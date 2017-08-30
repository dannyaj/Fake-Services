FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y python
RUN apt-get install -y python-pip
RUN pip install flask

ADD AuthServer.py /

CMD ["/usr/bin/python", "/AuthServer.py"]
