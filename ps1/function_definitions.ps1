
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

function Add-Python-Executable-To-Path {
    <#
    .SYNOPSIS
        Adds python's executable path associated with the environment to the PATH if necessary.
    .EXAMPLE
        Add-Python-Executable-To-Path $EnvironmentName
    #>
    [CmdletBinding(DefaultParameterSetName = 'EnvironmentName')]
    Param(
        [Parameter(Mandatory = $true, Position = 0, ValueFromPipeline = $true)]
        [string]$EnvironmentName
    )
	$ExecutablePath = "${HomeDirectory}\Anaconda3\envs\${EnvironmentName}\python.exe"
	$PathArray = $ExecutablePath -Split "\\"
	$PythonFolder = $PathArray[0..($PathArray.count - 2)] -Join "\"
	if (!($env:Path -Like "*$PythonFolder*")) {
		# Write-Host "The ${EnvironmentName} executable path is not in PATH" -ForegroundColor Red
		$env:Path = "${HomeDirectory}\Anaconda3\envs\${EnvironmentName};" + $env:Path
	}
}

function Get-Python-Version {
    <#
    .SYNOPSIS
        Get the version of python associated with the environment.
    .EXAMPLE
        $PythonVersion = Get-Python-Version $EnvironmentName
    #>
    [CmdletBinding(DefaultParameterSetName = 'EnvironmentName')]
    Param(
        [Parameter(Mandatory = $true, Position = 0, ValueFromPipeline = $true)]
        [string]$EnvironmentName
    )
	$CommandString = "${HomeDirectory}\Anaconda3\envs\${EnvironmentName}\python.exe --version"
	$PythonVersion = cmd /c $CommandString '2>&1'
	$PythonVersion = $PythonVersion.Trim()
	
	Return $PythonVersion
}

function Add-Kernel-To-Launcher {
    <#
    .SYNOPSIS
        Adds python's executable path associated with the environment to the PATH if necessary.
    .EXAMPLE
        Add-Kernel-To-Launcher $EnvironmentName -DisplayName $DisplayName
    #>
    [CmdletBinding(DefaultParameterSetName = 'EnvironmentName')]
    Param(
        [Parameter(Mandatory = $true, Position = 0, ValueFromPipeline = $true)]
        [string]$EnvironmentName,
		
        [Parameter(ParameterSetName = 'DisplayName')]
        [string]$DisplayName = "Python"
    )
	$PythonVersion = Get-Python-Version $EnvironmentName
	
	$ExecutablePath = "${HomeDirectory}\Anaconda3\envs\${EnvironmentName}\python.exe"
	
	# Fix LookupError: unknown encoding: cp65001
	$CommandString = -Join($ExecutablePath, ' -c "import os; os.environ[', "'PYTHONIOENCODING'", "] = 'UTF-8'", '"')
	# Write-Host "CommandString = '${CommandString}'" -ForegroundColor Gray
	Invoke-Expression $CommandString
	
	$CommandString = -Join($ExecutablePath, ' -m ipykernel install --user --name ', $EnvironmentName, ' --display-name "', $DisplayName, ' (', $PythonVersion, ')"')
	# Write-Host "CommandString = '${CommandString}'" -ForegroundColor Gray
	Invoke-Expression $CommandString
}

function Import-Workspace-File {
    <#
    .SYNOPSIS
        Import the local workspace file into the Juoyter Lab workspaces.
    .DESCRIPTION
        Returns the newly created workspace path.
    .EXAMPLE
        $WorkspacePath = Import-Workspace-File $RepositoryPath
    #>
    [CmdletBinding(DefaultParameterSetName = 'RepositoryPath')]
    Param(
        [Parameter(Mandatory = $true, Position = 0, ValueFromPipeline = $true)]
        [string]$RepositoryPath,
		
        [Parameter(ParameterSetName = 'RepositoriesDirectory')]
        [string]$RepositoriesDirectory = "${Env:UserProfile}\Documents\Repositories"
    )
	$OldPath = Get-Location
	cd $RepositoriesDirectory\$RepositoryPath
	$WorkspacePath = (jupyter-lab workspaces import workspace.json) | Out-String
	$WorkspacePath = $WorkspacePath.Trim()
	$WorkspacePath = $WorkspacePath -csplit ' '
	$WorkspacePath = $WorkspacePath[$WorkspacePath.Count - 1]
	cd $OldPath
	
	Return $WorkspacePath
}

function Get-Token-String {
    <#
    .SYNOPSIS
        Get the token string from the running Jupyter Lab.
    .EXAMPLE
        $TokenString = Get-Token-String
    #>
	$ListResults = (jupyter notebook list) | Out-String
	$TokenRegex = [regex] '(?m)http://localhost:8888/\?token=([^ ]+) :: '
	$TokenString = $TokenRegex.Match($ListResults).Groups[1].Value
	
	Return $TokenString
}