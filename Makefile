REPOSITORY := bi-framework
VERSION ?= commit_$(shell git rev-parse --short HEAD)
LOCAL_STACK=0.14.1
CREDENTIALS_VAR := test
PREBUILD_DATE := 2018-03-07
AWS_REGION := eu-west-1
ENVIRONMENT := test
AWS_IMAGE_ID := $(shell docker ps --filter ancestor=localstack/localstack:$(LOCAL_STACK) --format {{.ID}})
PACKAGE_NAME := handlers-pkg.$(VERSION).zip

export REPOSITORY
export VERSION
export CREDENTIALS_VAR
export PACKAGE_NAME
export LOCAL_STACK

COMPOSE_DEFAULT_FLAGS := -f docker-compose.yaml
COMPOSE_TEST_FLAGS := $(COMPOSE_DEFAULT_FLAGS) -f docker-compose.test.yaml


create-network:
	@echo "=>  Creating network 'lambda_bridge'"
	@docker network create -d bridge lambda_bridge 2>/dev/null || true

.PHONY: mock-aws
mock-aws: create-network
	@echo "=>  Creating aws resources"
	@if [ ! -z ${AWS_IMAGE_ID} ]; then\
    	docker stop $(AWS_IMAGE_ID); \
    	docker rm $(AWS_IMAGE_ID); \
	fi
	@docker-compose -f docker-compose.yaml run --rm aws-mock


validate-templates:
	aws --profile $(PROFILE) cloudformation validate-template --template-body file://infrastructure/cfn-$(PROJECT)-persistence.yaml --region $(AWS_REGION)

package_name:
	@echo $(PACKAGE_NAME)

%-persistence:
	aws --region $(AWS_REGION) --profile $(PROFILE) cloudformation $*-stack \
		--stack-name $(PROJECT)-persistence-$(ENVIRONMENT) \
		--capabilities CAPABILITY_IAM \
		--template-body file://infrastructure/cfn-$(PROJECT)-persistence.yaml \
		--parameters \
			ParameterKey=Environment,ParameterValue=$(ENVIRONMENT) \
		--tags \
			Key=Name,Value=$(PROJECT)-persistence \
			Key=Component,Value=$(PROJECT) \
			Key=Environment,Value=$(ENVIRONMENT) \
			Key=BusinessArea,Value=BusinessIntelligence \
			Key=InfrastructureType,Value=Storage \
			Key=Access,Value=Internal
	aws --region $(AWS_REGION) --profile $(PROFILE) cloudformation wait stack-$*-complete \
		--stack-name $(PROJECT)-persistence-$(ENVIRONMENT)


build-%:
	docker-compose $(COMPOSE_TEST_FLAGS) build $*

package-lambda:
	docker-compose $(COMPOSE_DEFAULT_FLAGS) run --rm package

setup-local-environment: package-lambda provision

unittests: build-unittests setup-local-environment
	docker-compose $(COMPOSE_TEST_FLAGS) run --rm unittests

unittests-watch: build-unittests setup-local-environment
	docker-compose $(COMPOSE_TEST_FLAGS) run --rm unittests-watch

systemtests: build-systemtests setup-local-environment
	docker-compose $(COMPOSE_TEST_FLAGS) run --rm systemtests

systemtests-watch: build-systemtests setup-local-environment
	docker-compose $(COMPOSE_TEST_FLAGS) run --rm systemtests-watch

tests: unit-test system-test

provision:
	docker-compose run provisioner

clear-pycache:
	sudo find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf

stop-containers:
	docker-compose $(COMPOSE_TEST_FLAGS) kill

clear-containers: stop-containers
	docker-compose $(COMPOSE_TEST_FLAGS) rm --force

stop-all-containers:
	docker ps -q | xargs -I@ docker stop @

clear-all-containers: stop-all-containers
	docker ps -aq | xargs -I@ docker rm @

clear-volumes: clear-all-containers
	docker volume ls -q | xargs -I@ docker volume rm @

clear-images: clear-volumes
	docker images -q | uniq | xargs -I@ docker rmi -f @
