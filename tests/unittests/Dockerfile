ARG ALPINE_VERSION=3.11
ARG PYTHON_VERSION=3.8.3
FROM python:${PYTHON_VERSION}-alpine${ALPINE_VERSION}

ARG PYPI_USERNAME
ARG PYPI_PASSWORD

RUN apk add --no-cache gettext
RUN pip install wheel

COPY awsmock-credentials /root/.aws/credentials
COPY . /usr/unittests
WORKDIR /usr/unittests

RUN pip install -r /usr/unittests/requirements.txt
ENV PYTHONPATH=$PYTHONPATH:/app/src

ENTRYPOINT ["py.test", "-c", "pytest.cfg"]
