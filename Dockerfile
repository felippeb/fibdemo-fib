FROM ubuntu:trusty

MAINTAINER felippe burk

RUN apt-get update
RUN apt-get install -y tar git curl wget dialog net-tools build-essential

RUN apt-get install -y python python-dev python-distribute python-pip libevent-dev

ADD fibapi /fibapi
ADD fibgen /fibgen

RUN pip install ./fibgen/ 
RUN pip install -r /fibapi/requirements.txt

EXPOSE 5000

WORKDIR /fibapi

CMD python /fibapi/server.py
