ARG PYTHON_VERSION=3.10.1
FROM python:${PYTHON_VERSION}-slim-buster as python-base
ARG AWS_ACCESS_KEY_ID \
    AWS_SECRET_ACCESS_KEY \
    SERVICENAME \
    ENVIRONMENT \
    AWS_CLI=1.22.41

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        groff \
        less \
        curl \
        jq\
    && pip --no-cache-dir install "awscli==${AWS_CLI}"  \
    && apt-get purge -y --auto-remove \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
    
WORKDIR /infrastructure
COPY . /infrastructure

RUN chmod 755 provision-localstack.sh

ENTRYPOINT [ "./provision-localstack.sh" ]
