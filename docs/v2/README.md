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
- Please create a PostgreSQL database in your local env and execute the [SQL](../../sql/create_tables.sql) to create the tables.
- change the database connection string in the file [SessionGenerator.py](../../src/v2/SessionGenerator.py) to your own database connection string or change the function `def __get_db_conn_str__(self)->str:`  in the file [SessionGenerator.py](../../src/v2/SessionGenerator.py). It's supposed to use environment variable to store the database connection string. But I don't want to expose my database connection string in the git repo. So, I just hard code it here.


#### 3.1.3. Run the project
- You can launch the project by the script `start.sh` or by the command `uvicorn`.
```bash
$ sh start.sh
```
or 
```python
$ uvicorn --port 8081  main:app --host 0.0.0.0  --reload --log-config conf/logging.conf
```

- Then, you can access the API by `http://localhost:8081/v2/vote` or `http://localhost:8081/v2/qa/`. You can test it with the command `curl`. The following is the response when receiving a valid request. As you can see here, status code is http `200` (OK) and a json string `{"id":ID, "status":"ok"}`.

```bash
# If you'd like to save a question/answer pair, you can use the following command.
$ curl --verbose  -H 'accept: application/json'   -H 'Content-Type: application/json'  -X POST http://localhost:8081/v2/qa/ -d '{"phone_number":"+886930900831", "query":"This is my question", "response":"a response"}'
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1:8081...
* Connected to localhost (127.0.0.1) port 8081 (#0)
> POST /v2/qa/ HTTP/1.1
> Host: localhost:8081
> User-Agent: curl/7.78.0
> accept: application/json
> Content-Type: application/json
> Content-Length: 88
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< date: Thu, 07 Dec 2023 04:09:11 GMT
< server: uvicorn
< content-length: 22
< content-type: application/json
< 
* Connection #0 to host localhost left intact
{"id":6,"status":"ok"}

# If you'd like to save a vote with phone number + query, you can use the following command.
$ curl --verbose  -H 'accept: application/json'   -H 'Content-Type: application/json'  -X POST http://localhost:8081/v2/vote/ -d '{"phone_number":"+886930900831", "query":"This is my question", "vote":"up"}'
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1:8081...
* Connected to localhost (127.0.0.1) port 8081 (#0)
> POST /v2/vote/ HTTP/1.1
> Host: localhost:8081
> User-Agent: curl/7.78.0
> accept: application/json
> Content-Type: application/json
> Content-Length: 76
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< date: Thu, 07 Dec 2023 04:09:48 GMT
< server: uvicorn
< content-length: 15
< content-type: application/json
< 
* Connection #0 to host localhost left intact
{"status":"ok"}
``` 

-  The following is the response when receiving an invalid request. As you can see here, status code is http `4XX` and some json formatted message.
```bash
$ curl  --verbose -X 'POST'   'http://localhost:8081/v2/vote/'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{  "phone_number": "+8869000000", "query":"QUESTION"}'
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1:8081...
* Connected to localhost (127.0.0.1) port 8081 (#0)
> POST /v2/vote/ HTTP/1.1
> Host: localhost:8081
> User-Agent: curl/7.78.0
> accept: application/json
> Content-Type: application/json
> Content-Length: 53
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 422 Unprocessable Entity
< date: Wed, 06 Dec 2023 03:44:25 GMT
< server: uvicorn
< content-length: 184
< content-type: application/json
< 
* Connection #0 to host localhost left intact
{"detail":[{"type":"missing","loc":["body","vote"],"msg":"Field required","input":{"phone_number":"+8869000000","query":"QUESTION"},"url":"https://errors.pydantic.dev/2.5/v/missing"}]}

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
- Because [docker-compose.yml](../../docker-compose.yml) already defined a postgresql DB, what you need to do is to execute the [SQL](../../sql/create_tables.sql) to create all tables.

#### 3.2.3 make sure the container is running
- check the container is running by the following command.
```bash
$ docker ps
CONTAINER ID   IMAGE                                   COMMAND                  CREATED          STATUS          PORTS                    NAMES
b67f9aa4ff8f   gogotechhk/gogobot-log-api:0.2.0        "sh start.sh"            14 seconds ago   Up 13 seconds   0.0.0.0:8081->8081/tcp   gogobot-log-api
7deb1d9f09f3   postgres                                "docker-entrypoint.s…"   24 hours ago     Up 13 seconds   0.0.0.0:5432->5432/tcp   gogobot-log-db
```
#### 3.2.4 Test it
- Please refer to the section `3.1.3` to test it.

#### 3.2.5 stop the container
- You can stop the container by the following command.
```bash
# if you'd like stop all containers defined in docker-compose.yml, you can use the following command.
$  docker-compose stop

# or you can use "make stop-all" to stop all containers defined in docker-compose.yml.
$ make stop-all
```

#### 3.2.6 other options
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
```


## 4. Test it with pytest
- Please start db container before running pytest.
```bash
$ make start-db
```
- Update the database connection string in the file [SessionGenerator.py](../../src/v2/SessionGenerator.py) to your own database connection string or change the function `def __get_db_conn_str__(self)->str:`  in the file [SessionGenerator.py](../../src/v2/SessionGenerator.py). Please use correct connection string.
- You can run pytest by the following command.
```bash
$ pytest test_main.py

```

