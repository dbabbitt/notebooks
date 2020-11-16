
function Format-Json {
    <#
    .SYNOPSIS
        Prettifies JSON output.
    .DESCRIPTION
        Reformats a JSON string so the output looks better than what ConvertTo-Json outputs.
    .PARAMETER Json
        Required: [string] The JSON text to prettify.
    .PARAMETER Minify
        Optional: Returns the json string compressed.
    .PARAMETER Indentation
        Optional: The number of spaces (1..1024) to use for indentation. Defaults to 4.
    .PARAMETER AsArray
        Optional: If set, the output will be in the form of a string array, otherwise a single string is output.
    .EXAMPLE
        $json | ConvertTo-Json | Format-Json -Indentation 2
    #>
    [CmdletBinding(DefaultParameterSetName = 'Prettify')]
    Param(
        [Parameter(Mandatory = $true, Position = 0, ValueFromPipeline = $true)]
        [string]$Json,

        [Parameter(ParameterSetName = 'Minify')]
        [switch]$Minify,

        [Parameter(ParameterSetName = 'Prettify')]
        [ValidateRange(1, 1024)]
        [int]$Indentation = 4,

        [Parameter(ParameterSetName = 'Prettify')]
        [switch]$AsArray
    )

    if ($PSCmdlet.ParameterSetName -eq 'Minify') {
        return ($Json | ConvertFrom-Json) | ConvertTo-Json -Depth 100 -Compress
    }

    # If the input JSON text has been created with ConvertTo-Json -Compress
    # then we first need to reconvert it without compression
    if ($Json -notmatch '\r?\n') {
        $Json = ($Json | ConvertFrom-Json) | ConvertTo-Json -Depth 100
    }

    $indent = 0
    $regexUnlessQuoted = '(?=([^"]*"[^"]*")*[^"]*$)'

    $result = $Json -split '\r?\n' |
        ForEach-Object {
            # If the line contains a ] or } character, 
            # we need to decrement the indentation level unless it is inside quotes.
            if ($_ -match "[}\]]$regexUnlessQuoted") {
                $indent = [Math]::Max($indent - $Indentation, 0)
            }

            # Replace all colon-space combinations by ": " unless it is inside quotes.
            $line = (' ' * $indent) + ($_.TrimStart() -replace ":\s+$regexUnlessQuoted", ': ')

            # If the line contains a [ or { character, 
            # we need to increment the indentation level unless it is inside quotes.
            if ($_ -match "[\{\[]$regexUnlessQuoted") {
                $indent += $Indentation
            }

            $line
        }

    if ($AsArray) { return $result }
    return $result -Join [Environment]::NewLine
}

$OldPath = Get-Location

# Update conda
Write-Host ""
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "                        Installing conda-build and compilers" -ForegroundColor Green
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
conda config --set auto_update_conda true
conda config --set report_errors false
conda install conda-build --yes
conda install m2w64-toolchain --yes
conda install mkl-service --yes
Write-Host ""
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "                               Updating base conda" -ForegroundColor Green
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
conda update --all --yes

# Create the conda environment
cd "C:\Users\dev\Documents\repositories\${RepositoryPath}"
Write-Host ""
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "                  Creating the ${DisplayName} conda environment" -ForegroundColor Green
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
conda env create
Write-Host ""
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "              Updating the ${DisplayName} conda environment" -ForegroundColor Green
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
conda env update --prune

# Add the kernel to the Launcher
Write-Host ""
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "                        Adding the kernel to the Launcher" -ForegroundColor Green
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
$CommandString = -Join('python -c "import sys;print(sys.executable)"')
# Write-Host "CommandString = ${CommandString}" -ForegroundColor Red
$ExecutablePath = Invoke-Expression $CommandString | Out-String
$ExecutablePath = $ExecutablePath.Trim()
# Write-Host "ExecutablePath = ${ExecutablePath}" -ForegroundColor Red
$EnvironmentRegex = [regex] "(?m)envs\\${EnvironmentName}"
if (!$EnvironmentRegex.IsMatch($ExecutablePath)) {
    $env:Path = "C:\Users\dev\Anaconda3\envs\${EnvironmentName};" + $env:Path
}
$CommandString = -Join($ExecutablePath, ' --version')
# Write-Host "CommandString = ${CommandString}" -ForegroundColor Red
$PythonVersion = cmd /c $CommandString '2>&1'
$PythonVersion = $PythonVersion.Trim()
# Write-Host "PythonVersion = ${PythonVersion}" -ForegroundColor Red
if (($PythonVersion -Eq "") -Or ($PythonVersion -Match '\]$')) {
    $PythonVersion = Invoke-Expression $CommandString | Out-String
    $PythonVersion = $PythonVersion.Trim()
}
$CommandString = -Join('python -m ipykernel install --user --name ', $EnvironmentName, ' --display-name "', $DisplayName, ' (', $PythonVersion, ')"')
# Write-Host "CommandString = ${CommandString}" -ForegroundColor Red
Invoke-Expression $CommandString
(Get-Content "C:\Users\dev\AppData\Roaming\jupyter\kernels\${EnvironmentName}\kernel.json") | ConvertFrom-Json | ConvertTo-Json -depth 7 | Format-Json -Indentation 2

# Add a workspace file for bookmarking
Write-Host ""
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "                        Importing the workspace file" -ForegroundColor Green
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
$WorkspacePath = (jupyter-lab workspaces import workspace.json) | Out-String
$WorkspacePath = $WorkspacePath.Trim()
Write-Host "${WorkspacePath}"
$WorkspacePath = $WorkspacePath -csplit ' '
$WorkspacePath = $WorkspacePath[$WorkspacePath.Count - 1]
(Get-Content $WorkspacePath) | ConvertFrom-Json | ConvertTo-Json -depth 7 | Format-Json -Indentation 2

# Clean up the mess
Write-Host ""
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "                          Cleaning the staging area" -ForegroundColor Green
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
jupyter-lab clean
Write-Host ""
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "                     Updating the Jupyter Lab extensions" -ForegroundColor Green
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
jupyter labextension update --all
Write-Host ""
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "                       Rebuilding the Jupyter Lab assets" -ForegroundColor Green
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
Copy-Item "C:\Users\dev\Documents\repositories\${RepositoryPath}\jupyter_notebook_config.py" -Destination "C:\Users\dev\.jupyter"
jupyter-lab build

cd $OldPath