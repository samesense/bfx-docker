FROM ubuntu:16.04

WORKDIR /

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update -y && \
    apt-get update --fix-missing && \
    apt-get install -y build-essential autotools-dev autoconf wget bzip2 ca-certificates curl git tar nano zlib1g-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
    
RUN wget https://github.com/torognes/vsearch/archive/v2.9.0.tar.gz && \
tar xzf v2.9.0.tar.gz && \
cd vsearch-2.9.0 && \
./autogen.sh && \
./configure  && \
make  && \
make install

ENV PATH /vsearch-2.9.0/bin/:$PATH
