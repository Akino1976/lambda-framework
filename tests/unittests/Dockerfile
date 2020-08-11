FROM python:3.7-alpine3.10

ARG PYPI_USERNAME
ARG PYPI_PASSWORD

RUN apk add --no-cache gettext
RUN pip install wheel


COPY . /usr/unittests
WORKDIR /usr/unittests

RUN pip install -r /usr/unittests/requirements.txt
ENV PYTHONPATH=$PYTHONPATH:/app/src

ENTRYPOINT ["py.test", "-c", "pytest.cfg"]
