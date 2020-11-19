
# Delete environment
Write-Host ""
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "                     Deleting the ${DisplayName} conda environment" -ForegroundColor Green
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
conda remove --name $EnvironmentName --all --yes

# You have to manually delete the folder if you don't manually stop the server
#jupyter notebook stop 8888
# Won't work on Windows as of 2020-11-19
If ([System.IO.File]::Exists($EnvironmentPath)) {
	Write-Host ""
	Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
	Write-Host "              Recursively removing ${EnvironmentPath}" -ForegroundColor Green
	Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
	Remove-Item -Recurse -Force $EnvironmentPath
}
conda info --envs