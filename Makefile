BASEDIR=~/gogobot-log-api
DOCKER_CMD=docker
TAG_VERSION=0.2.0

build:
	mkdir -p $(BASEDIR)/log
	chmod 1777 $(BASEDIR)/log
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
