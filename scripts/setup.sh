#! /bin/bash

cd Assesment-2
echo $PATH
sudo /home/jenkins/.local/bin/ansible-playbook -i ansible/inventory ansible/playbook.yaml