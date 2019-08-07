FROM ubuntu:latest
LABEL maintainer="chandra.ops3@gmail.com"

RUN apt-get update
RUN apt-get install python python-pip -y
RUN pip install requests
ADD ./mac-addr.py /root
USER root
WORKDIR /root
CMD ["/bin/bash"]

