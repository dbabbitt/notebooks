
$OldPath = Get-Location

# Create the temporary conda environment.yml file
conda config --set env_prompt '({name})'
cd "${RepositoriesDirectory}\${RepositoryPath}"
Write-Host ""
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "               Temporarily activating the ${EnvironmentName} environment" -ForegroundColor Green
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
conda activate $EnvironmentName
Write-Host ""
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "               Creating the temporary conda environment.yml file" -ForegroundColor Green
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
conda env export --name $EnvironmentName -f tmp_environment.yml
Write-Host ""
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "                    Deactivating the ${EnvironmentName} environment" -ForegroundColor Green
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
conda deactivate

cd $OldPath