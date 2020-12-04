#! /bin/bash

echo $PATH
pip3 install -r assesment2/requirements.txt
python3 -m pytest assesment2/service1 --cov assesment2/service1
python3 -m pytest assesment2/service2 --cov assesment2/service2
python3 -m pytest assesment2/service3 --cov assesment2/service3
python3 -m pytest assesment2/service4 --cov assesment2/service4