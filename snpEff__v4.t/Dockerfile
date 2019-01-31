FROM openjdk:8-slim

# snpeff
# Install libraries
RUN \
apt-get update && apt-get install -y --no-install-recommends \
build-essential \
ca-certificates \
libncurses5-dev \
libncursesw5-dev \
wget \
zlib1g-dev \
&& rm -rf /var/lib/apt/lists/*

# FROM continuumio/miniconda3
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH

RUN apt-get update --fix-missing && \
apt-get install -y wget bzip2 ca-certificates curl git && \
apt-get clean && \
rm -rf /var/lib/apt/lists/*

RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-4.5.11-Linux-x86_64.sh -O ~/miniconda.sh && \
/bin/bash ~/miniconda.sh -b -p /opt/conda && \
rm ~/miniconda.sh && \
/opt/conda/bin/conda clean -tipsy && \
ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
echo "conda activate base" >> ~/.bashrc

###############################################
# SciF Base
#
# docker build -t vanessa/cowsay .
# docker run vanessa/cowsay
#
###############################################

ENV DEBIAN_FRONTEND noninteractive

# Dependencies
RUN apt-get update && apt-get install -y wget \
                                         unzip \
                                         apt-utils \
                                         python

# Install scif from pypi
RUN /opt/conda/bin/pip install scif==0.0.75

# Install the filesystem from the recipe
ADD *.scif /
RUN scif install /recipe.scif

# SciF Entrypoint
ENTRYPOINT ["scif"]