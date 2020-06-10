

# Add it to the multi-host network
Write-Host ""
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "          	    Adding jupyterlab to the multi-host network" -ForegroundColor Green
Write-Host "---------------------------------------------------------------------------------" -ForegroundColor Green
docker network connect multi-host-network jupyterlab

# Inspect the network to see if it's on there
docker network inspect multi-host-network