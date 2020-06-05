FROM golang:1.14

# Set the Current Working Directory inside the container
WORKDIR $GOPATH/src/github.com/openshift-pipelines/

ENV GO111MODULE on
ENV CGO_ENABLED 0

# Install gauge

RUN apt-key adv --keyserver hkp://pool.sks-keyservers.net --recv-keys 023EDB0B || \
    apt-key adv --keyserver hkp://pool.sks-keyservers.net --recv-keys 023EDB0B || \
    apt-key adv --keyserver hkp://pool.sks-keyservers.net --recv-keys 023EDB0B && \
    echo deb https://dl.bintray.com/gauge/gauge-deb stable main | tee -a /etc/apt/sources.list

RUN apt-get update && apt-get install gauge

# Install go gauge plugins
RUN gauge install go && \
    gauge install html-report && \
    gauge install xml-report && \
	gauge install reportportal && \
    gauge config check_updates false && \
    gauge config runner_connection_timeout 3600000 && \
    gauge config runner_request_timeout 3600000 && \
    gauge config ide_request_timeout 3600000 && \
    gauge config plugin_connection_timeout 3600000 && \
    gauge config plugin_kill_timeout 3600000

ENV PATH=$HOME/.gauge:$PATH

# Install latest oc and kubectl clients
ADD scripts/openshift-install.sh /usr/local/bin/

RUN /usr/local/bin/openshift-install.sh