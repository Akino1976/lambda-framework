FROM app-framework as app
FROM python:3.7-alpine3.10

ARG BAMBORA_PYPI_USERNAME
ARG BAMBORA_PYPI_PASSWORD

RUN apk add --no-cache gettext
RUN pip install wheel

COPY --from=app /usr/app /usr/app

COPY . /usr/systemtests
WORKDIR /usr/systemtests

RUN pip install -r /usr/systemtests/requirements.txt
RUN pip install -r /usr/app/requirements.txt
ENV PYTHONPATH=$PYTHONPATH:/usr/src

EXPOSE 1433

ENTRYPOINT ["py.test", "-c", "pytest.cfg"]
