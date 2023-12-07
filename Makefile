BASEDIR=~/gogobot-log-api
DOCKER_CMD=docker
TAG_VERSION=0.2.0

build:
	mkdir -p $(BASEDIR)/log
	$(DOCKER_CMD) build -t gogotechhk/gogobot-log-api:$(TAG_VERSION) .

start-all:
	docker-compose up -d

start-db:
	docker-compose up -d db

stop-all:
	docker-compose stop

stop-db:
	docker-compose stop db
