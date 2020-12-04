#! /bin/bash

ssh swarm-manager << EOF
sudo docker pull jcashen/service1:latest
sudo docker pull jcashen/service2:latest
sudo docker pull jcashen/service3:latest
sudo docker pull jcashen/service4:latest
git clone https://github.com/JCashen/Assesment-2.git
cd Assesment-2/
sudo docker stack deploy --compose-file docker-compose.yaml gacha_app
EOF