FROM python:3.7-alpine3.10 as builder

ENV PYTHONUNBUFFERED=1
ENV S3_HOST=aws-mock:3000

ARG PYPI_USERNAME
ARG PYPI_PASSWORD

RUN apk add --no-cache gettext
RUN pip install wheel

COPY requirements.txt /tmp/requirements.txt
RUN pip wheel -w /wheelhouse -r /tmp/requirements.txt

FROM python:3.7-alpine3.10

COPY --from=builder /wheelhouse /wheelhouse
COPY requirements.txt /tmp/requirements.txt
COPY awsmock-credentials /root/.aws/credentials

RUN pip install -r /tmp/requirements.txt --no-index --find-links /wheelhouse

COPY . /systemtests
WORKDIR /systemtests

ENTRYPOINT ["py.test", "-c", "pytest.cfg"]
