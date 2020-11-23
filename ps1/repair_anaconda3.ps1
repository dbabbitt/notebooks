
# cd $Env:UserProfile\Documents\repositories\notebooks\ps1
# clear
# .\repair_anaconda3.ps1

$AnacondaName = "anaconda3"
$HomeDirectory = $Env:UserProfile
$AnacondaFolder = "${HomeDirectory}\${AnacondaName}"
$BackupName = "${AnacondaName}_old"
$BackupFolder = "${HomeDirectory}\${BackupFolder}"
#Remove-Item -Recurse -Force $BackupFolder
# THIS DELETED MY ENTIRE DEV FOLDER!!!
#Get-Childitem -Path $BackupFolder -Recurse | Remove-Item -Recurse -Force
If (Test-Path -Path $BackupFolder -PathType Container) {
	Read-Host "Delete or rename the ${BackupName} folder manually, then press ENTER to continue..."
}
If (!(Test-Path -Path $BackupFolder -PathType Container)) {
	Rename-Item $AnacondaFolder $BackupFolder
}
If (!(Test-Path -Path $AnacondaFolder -PathType Container)) {
	# $PathVargs = {C:\Users\dev\Downloads\Anaconda3-2020.07-Windows-x86_64.exe}
	# Invoke-Command -ScriptBlock $PathVargs
	Read-Host "Launch the Anaconda3 installer manually, then press ENTER to continue when it is complete..."
	cd $HomeDirectory
	robocopy $BackupName $AnacondaName /S
}

$CommandString = "jupyter notebook --version"
Write-Host "CommandString = ${CommandString}" -ForegroundColor Red
$VersionResults = cmd /c $CommandString '2>&1'
$VersionResults = $VersionResults.Trim()
Write-Host "VersionResults = ${VersionResults}" -ForegroundColor Red
