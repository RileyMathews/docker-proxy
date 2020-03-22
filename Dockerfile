FROM docker.pkg.github.com/rileymathews/docker-base-dev/docker-base-dev:4

RUN yum install python3 -y
RUN pip3 install jinja2

RUN yum install -y yum-utils
RUN yum-config-manager --add-repo https://getenvoy.io/linux/centos/tetrate-getenvoy.repo
RUN yum install -y getenvoy-envoy
WORKDIR /workdir
COPY ./resources/ ./resources/
CMD ["bash", "resources/entrypoint.sh"]
