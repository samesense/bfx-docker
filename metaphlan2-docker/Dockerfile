FROM ubuntu:18.04
MAINTAINER Francesco Beghini, francesco.beghini@unitn.it
ENV TOOLNAME metaphlan2 

ENV PACKAGES python-numpy python-biom-format python-biopython bowtie2 wget unzip make xz-utils ca-certificates mercurial python-yaml libsys-hostname-long-perl
RUN apt-get update -y 
RUN apt-get install -y --no-install-recommends ${PACKAGES}

ENV PREFIX /biobox/
RUN mkdir -p ${PREFIX}/src/ ${PREFIX}/bin/ ${PREFIX}/lib/ ${PREFIX}/share/ 
ENV PATH=${PREFIX}/bin:${PREFIX}/src/${TOOLNAME}:${PATH}

# Download MetaPhlan2 from BioBakery repo and install the DB
RUN hg clone https://bitbucket.org/biobakery/metaphlan2 ${PREFIX}/src/${TOOLNAME}
