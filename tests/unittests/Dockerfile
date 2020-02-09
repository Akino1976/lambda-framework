FROM app-framework  as app
FROM python:3.7-alpine3.10

ARG PYPI_USERNAME
ARG PYPI_PASSWORD

RUN apk add --no-cache gettext
RUN pip install wheel

COPY --from=app /usr/app /usr/app

COPY . /usr/unittests
WORKDIR /usr/unittests

RUN pip install -r /usr/unittests/requirements.txt
RUN pip install -r /usr/app/requirements.txt
ENV PYTHONPATH=$PYTHONPATH:/usr/app

ENTRYPOINT ["py.test", "-c", "pytest.cfg"]
