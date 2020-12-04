#! /bin/bash

pip3 install -r assesment2/requirements.txt
pytest assesment2/service1 --cov ./service1
pytest assesment2/service2 --cov ./service2
pytest assesment2/service3 --cov ./service3
pytest assesment2/service4 --cov ./service4