FROM python:3.6-alpine
MAINTAINER Perry Evans <https://github.com/samesense>

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh sqlite sqlite-dev sqlite-libs
RUN git clone https://github.com/kylebittinger/brocc
RUN cd brocc && pip install .
