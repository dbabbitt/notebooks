
# Get jupyter lab set up
$DisplayName = "COVID-19"
$RepositoryPath = "notebooks/covid19"
$EnvironmentName = "covid19"
."C:\Users\dev\Documents\repositories\notebooks\ps1\create_conda_environment.ps1"
Write-Host ""
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "                          Getting the Jupyter Lab token" -ForegroundColor Green
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
$TokenRegex = [regex] '(?m)http://0\.0\.0\.0:8888/\?token=([^ ]+) :: '
$ListResults = (jupyter notebook list) | Out-String
$TokenString = $TokenRegex.Match($ListResults).Groups[1].Value
Write-Host $ListResults

# Restart jupyter lab
jupyter lab

# Open the webpage in Chrome
Start-Process "chrome.exe" "http://localhost:8888/lab?clone=${EnvironmentName}&token=${TokenString}"