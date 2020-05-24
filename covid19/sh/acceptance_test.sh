
docker network create --subnet 172.20.0.0/16 --ip-range 172.20.240.0/20 multi-host-network

docker volume create --name jiraVolume

docker run -v jiraVolume:/var/atlassian/application-data/jira --name="jira" -d -p 8080:8080 -p 2990:2990 atlassian/jira-software

%% Bring up the browser and install the plugins

docker network ls

docker network connect --ip 172.20.240.1 multi-host-network jira

docker create --name curl -t -i curlimages/curl /bin/sh

docker start -a -i curl

docker network connect multi-host-network curl

docker network ls

docker network inspect multi-host-network

docker cp snapshot3.zip curl:tmp

cd tmp
ls

curl -u dbabbitt:d5b_QT@ASw@Kc2# -i -H "Content-Type: application/json" -X POST http://172.20.240.1:2990/jira/rest/configuration-manager/api/1.3/deployments -d '{"scope" : "system", "mode" : "systemRestore"}'

curl --user dbabbitt:d5b_QT@ASw@Kc2# --include --request PUT http://172.20.240.1:8080/rest/configuration-manager/api/1.3/deployments/1/content -F file=@snapshot3.zip