# FastAPIDemo
## 1. Project Introduction
This project is used to save all input into a file as long as it is a POST request.

## 2. Folder Structure
```
├── README.md: Introduction
├── main.py: main file
├── start.sh: the script to start the project
├── test_main.py: test file
├── Dockerfile: Dockerfile. Used to create gogobot-log-api docker image.
├── Makefile: Makefile
├── requirements.txt: necessary packages to run the project
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

#### 3.1.2. Run the project
- You can launch the project by the script `start.sh` or by the command `uvicorn`.
```bash
$ sh start.sh
```
or 
```python
$ uvicorn --port 8081  main:app --host 0.0.0.0  --reload --log-config conf/logging.conf
```

- Then, you can access the API by `http://localhost:8081/v2/vote` or `http://localhost:8081/v2/qa/`. You can test it with the command `curl`. The following is the response when receiving a valid request. As you can see here, status code is http `200` (OK) and a json string `{"status":"ok"}`.

```bash
# If you'd like to save a question/answer pair, you can use the following command.
$ curl -X 'POST' --verbose 'http://localhost:8081/v2/qa/'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{  "phone_number": "+8869000000", "query":"QUESTION HERE", "response":"RESPONSE HERE" }'
*   Trying 127.0.0.1:8081...
* Connected to localhost (127.0.0.1) port 8081 (#0)
> POST /v2/vote/ HTTP/1.1
> Host: localhost:8081
> User-Agent: curl/7.78.0
> accept: application/json
> Content-Type: application/json
> Content-Length: 87
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< date: Wed, 06 Dec 2023 03:42:57 GMT
< server: uvicorn
< content-length: 15
< content-type: application/json
< 
* Connection #0 to host localhost left intact
{"status":"ok"}

# If you'd like to save a vote, you can use the following command.
$ curl -X 'POST' --verbose  'http://localhost:8081/v2/vote/'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{  "phone_number": "+8869000000", "query":"QUESTION HERE", "vote":"UP/DOWN" }'
*   Trying 127.0.0.1:8081...
* Connected to localhost (127.0.0.1) port 8081 (#0)
> POST /v2/vote/ HTTP/1.1
> Host: localhost:8081
> User-Agent: curl/7.78.0
> accept: application/json
> Content-Type: application/json
> Content-Length: 87
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< date: Wed, 06 Dec 2023 03:42:57 GMT
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
$ docker build -t  gogotechhk/gogobot-log-api:0.2.0 .
```
#### 3.2.2 Run the docker image
- You can run the docker image by the following command.
```bash
$ make start-container
```
#### 3.2.3 make sure the container is running
- check the container is running by the following command.
```bash
$ docker ps
CONTAINER ID   IMAGE                                   COMMAND         CREATED         STATUS         PORTS                    NAMES
629ba0e57926   gogotechhk/gogobot-log-api:0.2.0        "sh start.sh"   7 minutes ago   Up 7 minutes   0.0.0.0:8081->8081/tcp   gogobot-log-api
```
#### 3.2.4 Test it
- Please refer to the section `3.1.2` to test it.

#### 3.2.5 stop the container
- You can stop the container by the following command.
```bash
$ make stop-container
```

## 4. Test it with pytest
- You don't need to start anything. Just run the following command.
```bash
$ pytest test_main.py

```

