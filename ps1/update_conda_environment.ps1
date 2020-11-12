
# Create the conda environment
$OldPath = Get-Location
cd "C:\Users\dev\Documents\repositories\${RepositoryPath}"
Write-Host ""
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "              Updating the ${DisplayName} conda environment" -ForegroundColor Green
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
conda env update --prune

cd $OldPath