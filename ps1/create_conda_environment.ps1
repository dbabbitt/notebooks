
."${RepositoriesDirectory}\notebooks\ps1\function_definitions.ps1"

$OldPath = Get-Location

# Update conda
conda config --set auto_update_conda true
conda config --set report_errors false
<# Write-Host ""
Write-Host "-------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "                              Installing conda-build" -ForegroundColor Green
Write-Host "-------------------------------------------------------------------------------" -ForegroundColor Green
conda install conda-build --yes
Write-Host ""
Write-Host "-------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "                             Installing m2w64-toolchain" -ForegroundColor Green
Write-Host "-------------------------------------------------------------------------------" -ForegroundColor Green
conda install m2w64-toolchain --yes
Write-Host ""
Write-Host "-------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "                              Installing mkl-service" -ForegroundColor Green
Write-Host "-------------------------------------------------------------------------------" -ForegroundColor Green
conda install mkl-service --yes #>
Write-Host ""
Write-Host "-------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "              Checking all base conda packages for potential updates" -ForegroundColor Green
Write-Host "-------------------------------------------------------------------------------" -ForegroundColor Green
conda update --all --yes

# Create the conda environment
."${RepositoriesDirectory}\${RepositoryPath}\ps1\update_conda_environment.ps1"

# Add the kernel to the Launcher
Write-Host ""
Write-Host "-------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "                        Adding the kernel to the Launcher" -ForegroundColor Green
Write-Host "-------------------------------------------------------------------------------" -ForegroundColor Green
Add-Python-Executable-To-Path $EnvironmentName
Add-Kernel-To-Launcher $EnvironmentName -DisplayName $DisplayName
$KernelPath = "${HomeDirectory}\AppData\Roaming\jupyter\kernels\${EnvironmentName}\kernel.json"
If (Test-Path -Path $KernelPath -PathType Leaf) {
	(Get-Content $KernelPath) | ConvertFrom-Json | ConvertTo-Json -depth 7 | Format-Json -Indentation 2
}

# Add a workspace file for bookmarking
Write-Host ""
Write-Host "-------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "                        Importing the workspace file" -ForegroundColor Green
Write-Host "-------------------------------------------------------------------------------" -ForegroundColor Green
$WorkspacePath = Import-Workspace-File $RepositoryPath
If (Test-Path -Path $WorkspacePath -PathType Leaf) {
	(Get-Content $WorkspacePath) | ConvertFrom-Json | ConvertTo-Json -depth 7 | Format-Json -Indentation 2
}

# Clean up the mess
Write-Host ""
Write-Host "-------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "                          Cleaning the staging area" -ForegroundColor Green
Write-Host "-------------------------------------------------------------------------------" -ForegroundColor Green
jupyter-lab clean

# (Deprecated) Updating extensions with the jupyter labextension update command is now deprecated and will be removed
# in a future major version of JupyterLab.
<# $CommandString = "jupyter labextension list"
$ExtensionsList = Invoke-Expression $CommandString
if (!($ExtensionsList -Like "*No installed extensions*")) {
	Write-Host ""
	Write-Host "-------------------------------------------------------------------------------" -ForegroundColor Green
	Write-Host "                     Updating the Jupyter Lab extensions" -ForegroundColor Green
	Write-Host "-------------------------------------------------------------------------------" -ForegroundColor Green
	jupyter labextension update --all
} #>

Write-Host ""
Write-Host "-------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "                       Rebuilding the Jupyter Lab assets" -ForegroundColor Green
Write-Host "-------------------------------------------------------------------------------" -ForegroundColor Green
$OldConfigPath = "${HomeDirectory}\.jupyter\old_jupyter_notebook_config.py"
If (Test-Path -Path $OldConfigPath -PathType Leaf) {
	Read-Host "You better rescue your old_jupyter_notebook_config.py in the .jupyter folder, we are about to overwrite it. Then press ENTER to continue..."
}
$NewConfigPath = "${HomeDirectory}\.jupyter\jupyter_notebook_config.py"
Copy-Item $NewConfigPath -Destination $OldConfigPath
$ConfigPath = "${RepositoriesDirectory}\${RepositoryPath}\jupyter_notebook_config.py"
If (Test-Path -Path $ConfigPath -PathType Leaf) {
	Copy-Item $ConfigPath -Destination $NewConfigPath
}
jupyter-lab build

cd $OldPath