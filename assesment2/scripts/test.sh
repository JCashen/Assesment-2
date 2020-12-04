#! /bin/bash

pip3 install -r assesment2/requirements.txt
pytest ./service1 --cov ./service1
pytest ./service2 --cov ./service2
pytest ./service3 --cov ./service3
pytest ./service4 --cov ./service4