
# cd $Env:UserProfile\Documents\Repositories\notebooks\ps1
# clear
# .\test.ps1

$CommandString = "conda list -n myenv"
Write-Host "CommandString = ${CommandString}" -ForegroundColor Red
$ResultString = cmd /c $CommandString '2>&1'
$ResultString = $ResultString.Trim()
Write-Host "ResultString = ${ResultString}" -ForegroundColor Red