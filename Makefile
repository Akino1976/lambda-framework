PROJECT := app-framework
VERSION ?= commit_$(shell git rev-parse --short HEAD)
COMPOSE_FLAGS := -f docker-compose.yml
COMPOSE_TEST_FLAGS := $(COMPOSE_FLAGS) -f docker-compose.test.yml
CREDENTIALS_VAR := test
PREBUILD_DATE := 2018-03-07

export PROJECT
export VERSION
export CREDENTIALS_VAR

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

unittest: build-app mock-provision
	docker-compose $(COMPOSE_TEST_FLAGS) run --rm unittest

unittest-watch: build-app mock-provision
	docker-compose $(COMPOSE_TEST_FLAGS) run --rm unittest-watch

systemtests: run-detached build-systemtests-base mock-provision
	docker-compose $(COMPOSE_TEST_FLAGS) run --rm systemtests

systemtests-watch: run-detached build-systemtests-base mock-provision
	docker-compose $(COMPOSE_TEST_FLAGS) run --rm systemtests-watch


tests: unit-test system-test

mock-provision: build-provisioner
	docker-compose $(COMPOSE_FLAGS) run --rm provisioner

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

create-persistence:
	aws cloudformation create-stack --template-body file://infrastructure/cfn-bi-framework.persistence.yml \
	--stack-name lambda-framework \
	--profile aws-private \
	--region eu-west-1
