BASEDIR=~/gogobot-log-api
DOCKER_CMD=docker
TAG_VERSION=0.2.0

build:
	$(DOCKER_CMD) build -t gogotechhk/gogobot-log-api:$(TAG_VERSION) .
start-container:#
	mkdir -p $(BASEDIR)/log
	$(DOCKER_CMD) run -d -p 8081:8081 --rm -v $(BASEDIR)/log:/opt/log  --name gogobot-log-api gogotechhk/gogobot-log-api:$(TAG_VERSION)
stop-container:
	$(DOCKER_CMD) stop gogobot-log-api