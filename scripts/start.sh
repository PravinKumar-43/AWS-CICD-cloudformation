#!/bin/bash

cd /root/calculator

docker stop calculator || true
docker rm calculator || true

docker build -t calculator-application .

docker run -d -p 7000:5000 --name calculator calculator-application
