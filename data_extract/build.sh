#! /bin/bash

# This script builds a docker image with UQM code, 
# compiles UQM code (docker run)
# and copies result to output

docker build -t uqm_debug:latest .
docker run --name=uqm_instance uqm_debug 


container_id=$(docker ps -a -f status=exited -q)
docker cp "${container_id}:/usr/uqm/" output
docker rm $(docker ps -a -f status=exited -q)
