BASEDIR=~/gogobot-log-api
DOCKER_CMD=docker

build:
	$(DOCKER_CMD) build -t gogotechhk/gogobot-log-api:0.1.0 .
start-container:
	mkdir -p $(BASEDIR)/log
	$(DOCKER_CMD) run -d -p 8081:8081 --rm -v $(BASEDIR)/log:/opt/log  --name gogobot-log-api gogotechhk/gogobot-log-api:0.1.0
stop-container:
	$(DOCKER_CMD) stop gogobot-log-api