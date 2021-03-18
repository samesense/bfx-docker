# base image
FROM compbio/prsice:1.1

# Set correct environment variables.
ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive

# Remain current
RUN apt-get update --fix-missing && apt-get dist-upgrade -y --fix-missing

RUN cd /opt/ && wget -q https://cmake.org/files/v3.6/cmake-3.6.2-Linux-x86_64.sh && \
    mkdir /opt/cmake && \
    sh /opt/cmake-3.6.2-Linux-x86_64.sh --prefix=/opt/cmake --skip-license && \
    ln -s /opt/cmake/bin/cmake /usr/local/bin/cmake && \
    cmake --version && \
    rm -fr /opt/cmake-3.6.2-Linux-x86_64.sh

COPY fmsb_0.5.1.tar.gz /usr/local/pipeline/

RUN chmod -R 777 /usr/local/pipeline && \
	R CMD INSTALL /usr/local/pipeline/fmsb_0.5.1.tar.gz

RUN R -e "install.packages('data.table', repos='https://Rdatatable.gitlab.io/data.table', dependencies=TRUE)"

# prsice
RUN cd /usr/local/pipeline/ && git clone https://github.com/choishingwan/PRSice

RUN cd /usr/local/pipeline/PRSice && \
    chmod 777 PRSice.R && \
    cp -v PRSice.R /usr/local/bin && \
    mkdir build && cd build && cmake ../ && make && \
    chmod 777 ../bin/PRSice && \
    cp -v ../bin/PRSice /usr/local/bin/PRSice_linux && \
    cp -v ../bin/PRSice /usr/local/bin/

#-------------------------------PERMISSIONS--------------------------
RUN chmod -R 777 /usr/local/pipeline
RUN chown -R pipeman:ngsgroup /usr/local/pipeline

#---------------------------------------------------------------------
#Cleanup the temp dir
RUN rm -rf /tmp/*

#open ports private only
EXPOSE 8080

# Use baseimage-docker's bash.
CMD ["/bin/bash"]

#Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN apt-get autoclean && apt-get autoremove -y && rm -rf /var/lib/{apt,dpkg,cache,log}/
