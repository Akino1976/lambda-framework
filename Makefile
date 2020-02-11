PROJECT := bi-framework
VERSION ?= commit_$(shell git rev-parse --short HEAD)

CREDENTIALS_VAR := test
PREBUILD_DATE := 2018-03-07

PROFILE := solita
AWS_REGION := eu-west-1
ENVIRONMENT := test

PACKAGE_NAME := handlers-pkg.$(VERSION).zip

export PROJECT
export VERSION
export CREDENTIALS_VAR
export PACKAGE_NAME

COMPOSE_DEFAULT_FLAGS := -f docker-compose.yaml
COMPOSE_TEST_FLAGS := $(COMPOSE_DEFAULT_FLAGS) -f docker-compose.test.yaml

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

run-local: build-app
	docker-compose $(COMPOSE_FLAGS) run --rm app

run-python:
	docker-compose $(COMPOSE_FLAGS) run --rm init-python

run-detached: build-app
	docker-compose $(COMPOSE_FLAGS) run -d app

run-storage:
	docker-compose $(COMPOSE_FLAGS) run --rm storage

package-lambda:
	docker-compose $(COMPOSE_DEFAULT_FLAGS) run --rm package

setup-local-environment: package-lambda provision

unittest: build-app mock-provision
	docker-compose $(COMPOSE_TEST_FLAGS) run --rm unittest

unittest-watch: build-app mock-provision
	docker-compose $(COMPOSE_TEST_FLAGS) run --rm unittest-watch

systemtests: build-systemtests setup-local-environment
	docker-compose $(COMPOSE_TEST_FLAGS) run --rm --service-ports systemtests

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
