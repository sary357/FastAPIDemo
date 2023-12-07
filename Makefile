BASEDIR=~/gogobot-log-api
DOCKER_CMD=docker
TAG_VERSION=0.2.0

build:
	mkdir -p $(BASEDIR)/log
	$(DOCKER_CMD) build -t gogotechhk/gogobot-log-api:$(TAG_VERSION) .
