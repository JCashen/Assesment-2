#! /bin/bash

ssh jenkins@swarm-master << EOF
docker pull jcashen/service1:latest
docker pull jcashen/service2:latest
docker pull jcashen/service3:latest
docker pull jcashen/service4:latest
git clone https://github.com/JCashen/Assesment-2.git
cd Assesment-2/
docker stack deploy --compose-file docker-compose.yaml gacha_app
EOF