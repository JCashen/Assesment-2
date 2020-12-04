#! /bin/bash

echo $PATH
ansible-playbook -i ansible/inventory ansible/playbook.yaml