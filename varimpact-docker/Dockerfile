
FROM rocker/r-base

RUN apt-get update \
    && apt-get install -y git sudo aptitude curl libcurl4-openssl-dev libxml2-dev libssl-dev

ADD https://raw.githubusercontent.com/samesense/bfx-docker/master/varimpact-docker/install.R ./install.R

RUN Rscript install.R
