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
RUN metaphlan2.py --install

ENV VALIDATOR /bbx/validator/
ENV BASE_URL https://s3-us-west-1.amazonaws.com/bioboxes-tools/validate-biobox-file
ENV VERSION  0.x.y
RUN mkdir -p ${VALIDATOR}

# download the validate-biobox-file binary and extract it to the directory $VALIDATOR
RUN wget \
      --quiet \
      --output-document -\
      ${BASE_URL}/${VERSION}/validate-biobox-file.tar.xz \
    | tar xJf - \
      --directory ${VALIDATOR} \
      --strip-components=1

ENV PATH ${PATH}:${VALIDATOR}

#download yaml schema
RUN wget -q -O ${PREFIX}/share/schema.yaml https://raw.githubusercontent.com/bioboxes/rfc/master/container/profiling/schema.yaml

ADD mp2DockerUtils.py ${PREFIX}/bin/

##run the one time mapping from "species2genomes.txt" into NCBI taxids and store the result in $MAPPERRESULT
##since the NCBI taxonomy is not static, it might happen that some taxids are no longer used, i.e. the following program crashes. Try to manually update the XML files via the NCBI batch entrez system.
#ADD species2genomes.txt ${PREFIX}/src/${TOOLNAME}/utils/
#RUN perl -I ${PREFIX}/lib/ ${PREFIX}/bin/${MAPPERNAME}.pl ${PREFIX}/src/${TOOLNAME}/utils/species2genomes.txt ${PREFIX}/share/${MAPPERNAME}/workdir > ${MAPPERRESULT} 
##should the previous command be successful, temporary files in workdir/Downloads can be deleted
#RUN rm -rf ${PREFIX}/share/${MAPPERNAME}/workdir

ENV YAML "/bbx/mnt/input/biobox.yaml"
ENTRYPOINT ["mp2DockerUtils.py"]
