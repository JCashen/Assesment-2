#! /bin/bash

ssh swarm-manager << EOF
sudo docker pull jcashen/app-1:latest
sudo docker pull jcashen/app-2:latest
sudo docker pull jcashen/app-3:latest
sudo docker pull jcashen/app-4:latest
git clone https://github.com/JCashen/Assesment-2.git
cd Assesment-2/
sudo docker stack deploy --compose-file docker-compose.yaml gacha_app
EOF