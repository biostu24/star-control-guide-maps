# Base image
FROM debian
FROM gcc:4.9

# Dependencies 
RUN apt update
RUN apt install make
RUN apt install bash
RUN apt-get install libsdl1.2-dev -y
RUN apt-get install libsdl-image1.2 -y
RUN apt-get install libsdl-image1.2-dev -y
RUN apt-get install libmikmod-dev -y
RUN apt-get install libmikmod-config -y
RUN apt-get install libvorbis-dev -y
RUN apt-get install libogg-dev -y

# COPY files
COPY uqm /usr/uqm
COPY docker_entrypoint.sh /

# Check UQM directory 
RUN ls /usr/uqm

# UQM build
ENTRYPOINT ["bash", "docker_entrypoint.sh"]
