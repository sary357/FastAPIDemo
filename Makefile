BASEDIR=~/gogobot-log-api
DOCKER_CMD=docker
TAG_VERSION=0.3.2

build:
	$(DOCKER_CMD) build -t gogotechhk/gogobot-log-api:$(TAG_VERSION) .

start-all:
	docker-compose up -d

start-db:
	docker-compose up -d db

start-api:
	docker-compose up -d api

stop-all:
	docker-compose stop

stop-db:
	docker-compose stop db

stop-api:
	docker-compose stop api
