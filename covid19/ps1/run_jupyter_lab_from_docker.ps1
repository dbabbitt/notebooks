
$ContainerName = "jupyterlab"
$PullName = "jupyter/all-spark-notebook"
$DockerImages = (docker images --filter "reference=${PullName}" --format "{{.ID}}") | Out-String
$ImageID = $DockerImages.Trim()
if (!$ImageID) {
	Write-Host ""
	Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Yellow
	Write-Host "                       Pulling ${PullName} from docker hub" -ForegroundColor Yellow
	Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Yellow
	docker pull $PullName
	$DockerImages = (docker images --filter "reference=${PullName}" --format "{{.ID}}") | Out-String
	$ImageID = $DockerImages.Trim()
	if (!$ImageID) {
		$ImageID = 'e98729e5aea8'
	}
}
docker images --filter "reference=${PullName}"

# Multi-session server: just create an interactive container
# No start but named for future reference
$DockerContainers = (docker ps --filter "name=${ContainerName}" --format "{{.Image}}") | Out-String
$DockerContainers = $DockerContainers.Trim()
if ($DockerContainers -ne $ImageID) {
	Write-Host ""
	Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Yellow
	Write-Host "          	        Creating the interactive container" -ForegroundColor Yellow
	Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Yellow
	docker create -it --rm --publish 8888:8888 --publish 4040:4040 --user root --env JUPYTER_ENABLE_LAB=yes --env CONDA_AUTO_UPDATE_CONDA=true --env NB_GID=100 --env GRANT_SUDO=yes --volume D:\Documents\Repositories:/home/jovyan/repos --name $ContainerName $ImageID
}
docker ps --filter "name=${ContainerName}"

# Now start it
Write-Host ""
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "          	         Restarting the ${ContainerName} container" -ForegroundColor Green
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
docker restart $ContainerName

# Add it to the multi-host network
."D:\Documents\Repositories\data-foundations\ps1\add_${ContainerName}_to_network.ps1"

# Upgrade the operating system
docker exec -it -w /home/jovyan/repos/data-foundations/sh $ContainerName /bin/bash -c "bash upgrade_${ContainerName}.sh"

# Restart jupyter lab
docker exec -it ${ContainerName} /bin/bash -c "sudo initctl restart jupyter-server --no-wait"
#docker exec -it ${ContainerName} /opt/conda/bin/jupyter lab

# Get jupyter lab set up
$DisplayName = "COVID-19"
$RepositoryPath = "notebooks/covid19"
$EnvironmentName = "covid19"
."D:\Documents\Repositories\data-foundations\ps1\create_conda_environment.ps1"
Write-Host ""
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "          	            Getting the Jupyter Lab token" -ForegroundColor Green
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
$TokenRegex = [regex] '(?m)http://0\.0\.0\.0:8888/\?token=([^ ]+) :: /home/jovyan'
$ListResults = (docker exec -it ${ContainerName} /opt/conda/bin/jupyter notebook list) | Out-String
$TokenString = $TokenRegex.Match($ListResults).Groups[1].Value
Write-Host $ListResults

# Open the webpage in Chrome
Start-Process "chrome.exe" "http://localhost:8888/lab?clone=${EnvironmentName}&token=${TokenString}"