#!/bin/bash

cd /home/ec2-user/calculator-app

docker stop calculator || true
docker rm calculator || true

docker build -t calculator-application .

docker run -d -p 5000:5000 --name calculator calculator-application
