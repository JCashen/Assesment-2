#! /bin/bash

echo $PATH
pip3 install pytest pytest-cov
python3 -m pytest assesment2/service1 --cov ./service1
python3 -m pytest assesment2/service2 --cov ./service2
python3 -m pytest assesment2/service3 --cov ./service3
python3 -m pytest assesment2/service4 --cov ./service4