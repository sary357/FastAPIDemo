# FastAPIDemo
## 1. Project Introduction
This project is used to save all input into a file as long as it is a POST request.

## 2. Folder Structure
```
├── README.md: Introduction
├── docs
|   ├── v1
|   |   └── README.md: README.md for v1
|   └── v2
|       └── README.md: README.md for v2
|── src
|   └── v2
|       ├── SessionGenerator.py: generate database session
|       └── voteProcessor.py: deal with vote request and save it into database
├── main.py: main file
├── start.sh: the script to start the project
├── test_main.py: test file
├── Dockerfile: Dockerfile. Used to create gogobot-log-api docker image.
├── Makefile: only for creating gogobot-log-api docker image. 
├── requirements.txt: necessary packages to run the project
|── docker-compose.yml: docker-compose.yml. Used to create gogobot-log-api docker image and gogobot-log-db docker image.
├── scripts
|   └── process_log.py: extract user input from the log file. This is only for v1.
├── conf
|   └── logging.conf: logging configuration file
└── sql
    └── create_tables.sql: create initial db. You can use it to create db in your local environment.

```

## 3. How can I run it?
### 3.1. Run it locally
#### 3.1.1. checkout from git report and Install the dependencies
```bash
$ git clone GIT_PROJECT_URL
$ cd FastAPIDemo
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

#### 3.1.2. prepare the database
- Please create a PostgreSQL database in your local env and execute the `create_tables.sql` to create the tables.
- make sure `DB_CONN_STR`, `POSTGRES_USER`, and `POSTGRES_PASSWORD` are correct in the file `docker-compose.yml` according to your env.

#### 3.1.3. Run the project
- You can launch the project by the script `start.sh` or by the command `uvicorn`.
```bash
$ sh start.sh
```
 
```python
$ uvicorn --port 8081  main:app --host 0.0.0.0  --reload --log-config conf/logging.conf
```

### 3.2 Run it in docker
#### 3.2.1 Build docker image
- You can build the docker image by the following command.
```bash
# TAG_VERION is the version of the docker image like 0.2.0
$ docker build -t  gogotechhk/gogobot-log-api:TAG_VERSION .

# or you can udpate TAG_VERSION defined in Makefile, then use "make build" to build the docker image.
$ make build
```
#### 3.2.2 Run the docker image
- You can run the docker image by the following command.
```bash
# if you'd like start all containers defined in docker-compose.yml, you can use the following command.
$ docker-compose up -d

# or you can use "make start-all" to start all containers defined in docker-compose.yml.
$ make start-all
```
#### 3.2.3 create table schema
- Because `docker-compose.yml` already defined a postgresql DB container, what you need to do is to execute the `create_tables.sql` to create all tables.

#### 3.2.3 make sure the container is running
- check the container is running by the following command.
```bash
$ docker ps
CONTAINER ID   IMAGE                                   COMMAND                  CREATED          STATUS          PORTS                    NAMES
b67f9aa4ff8f   gogotechhk/gogobot-log-api:0.2.0        "sh start.sh"            14 seconds ago   Up 13 seconds   0.0.0.0:8081->8081/tcp   gogobot-log-api
7deb1d9f09f3   postgres                                "docker-entrypoint.s…"   24 hours ago     Up 13 seconds   0.0.0.0:5432->5432/tcp   gogobot-log-db
```

#### 3.2.4 stop the container
- You can stop the container by the following command.
```bash
# if you'd like stop all containers defined in docker-compose.yml, you can use the following command.
$  docker-compose stop

# or you can use "make stop-all" to stop all containers defined in docker-compose.yml.
$ make stop-all
```

#### 3.2.5 other options
- If you hope to execute/stop db container separately, you can use the following commands.
```bash
# start db container
$ docker-compose up -d db

# or you can use "make start-db" to start db container.
$ make start-db

# stop db container
$ docker-compose stop db

# or you can use "make start-db" to start db container.
$ make stop-db

# start api container
$ docker-compose up -d api

# or you can use "make start-api" to start db container.
$ make start-api

# stop api container
$ docker-compose stop api

# or you can use "make start-api" to start db container.
$ make stop-api
```


## 4. Test it with pytest
- Please start db container before running pytest.
```bash
$ make start-db
```
- make sure `DB_CONN_STR`, `POSTGRES_USER`, and `POSTGRES_PASSWORD` are correct in the file `docker-compose.yml` according to your env.
- You can run pytest by the following command. btw, my test cases so far only support v2.
```bash
$ pytest test_main.py

```


## How can I test v1 and v2 API? ##
- v1: 
  - [README.md](docs/v1/README.md)
- v2:
  - [README.md](docs/v2/README.md)