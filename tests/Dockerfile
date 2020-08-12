FROM akino1976/lambda-server

ENV PYTHONUNBUFFERED=1
ENV S3_HOST=aws-mock:3000
ENV ENVIRONMENT=docker
ENV VERSION=${VERSION}
ENV AWS_REGION=${AWS_REGION}
ENV APP_LOG_STYLE=text
ENV APP_NAME: medhelp-fuse
ENV APP_COMPONENT=data_integration
ENV INPUT_BUCKET=bi-framework-data-lake-docker-eu-west-1
ENV PACKAGE_NAME=${PACKAGE_NAME}

COPY ./tools/awsmock-credentials /root/.aws/credentials
