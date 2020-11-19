
# cd C:\Users\dev\Documents\repositories\notebooks\ps1
# clear
# .\repair_anaconda3.ps1

$AnacondaName = "anaconda3"
$DevFolder = "C:\Users\dev"
$AnacondaFolder = "${DevFolder}\${AnacondaName}"
$BackupName = "${AnacondaName}_old"
$BackupFolder = "${DevFolder}\${BackupFolder}"
#Remove-Item -Recurse -Force $BackupFolder
# THIS DELETED MY ENTIRE DEV FOLDER!!!
#Get-Childitem -Path $BackupFolder -Recurse | Remove-Item -Recurse -Force
If (!(Test-Path $BackupFolder)) {
	Rename-Item $AnacondaFolder $BackupFolder
}
If (!(Test-Path $AnacondaFolder)) {
	$PathVargs = {C:\Users\dev\Downloads\Anaconda3-2020.07-Windows-x86_64.exe}
	Invoke-Command -ScriptBlock $PathVargs
	cd $DevFolder
	robocopy $BackupName $AnacondaName /S
}

$CommandString = "jupyter notebook --version"
Write-Host "CommandString = ${CommandString}" -ForegroundColor Red
$VersionResults = cmd /c $CommandString '2>&1'
$VersionResults = $VersionResults.Trim()
Write-Host "VersionResults = ${VersionResults}" -ForegroundColor Red
