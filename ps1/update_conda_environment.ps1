
# Create the conda environment
cd "${RepositoriesDirectory}\${RepositoryPath}"
Write-Host ""
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
# Assume here that if the environment folder is missing, the environment was already deleted
If (Test-Path -Path $EnvironmentPath -PathType Container) {
	#Write-Host "${EnvironmentName} is a conda environment." -ForegroundColor Red
	Write-Host "                Updating the ${DisplayName} conda environment" -ForegroundColor Green
} Else {
	#Write-Host "${EnvironmentName} is not a conda environment." -ForegroundColor Green
	Write-Host "                Creating the ${DisplayName} conda environment" -ForegroundColor Green
}
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
conda env update --file environment.yml --prune
conda info --envs