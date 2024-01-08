# 1. How can I use v2?
- After launching local development env with no docker, then you can access v2 API by `http://localhost:8081/v2/vote` or `http://localhost:8081/v2/qa/`. You can test it with the command `curl`. The following is the response when receiving a valid request. As you can see here, status code is http `200` (OK) and a json string `{"id":ID, "status":"ok"}`.

```bash
# If you'd like to save a question/answer pair, you can use the following command.
$ curl --verbose  -H 'accept: application/json'   -H 'Content-Type: application/json'  -X POST http://localhost:8081/v2/qa/ -d '{"phone_number":"+886930900831", "question":"This is my question", "answer":"a answer"}'
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


# If you'd like to save a vote with phone number + question, you can use the following command.
$ curl --verbose  -H 'accept: application/json'   -H 'Content-Type: application/json'  -X POST http://localhost:8081/v2/vote/ -d '{"phone_number":"+886930900831", "question":"This is my question",  "answer":"a answer","vote":"up"}'
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


# If you'd like to save a vote with id + vote, you can use the following command.
$ curl --verbose  -H 'accept: application/json'  -H 'Content-Type: application/json'  -X POST http://localhost:8081/v2/vote/ -d '{"id":6, "vote":"up"}'
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1:8081...
* Connected to localhost (127.0.0.1) port 8081 (#0)
> POST /v2/vote/ HTTP/1.1
> Host: localhost:8081
> User-Agent: curl/7.78.0
> accept: application/json
> Content-Type: application/json
> Content-Length: 21
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< date: Thu, 07 Dec 2023 08:15:16 GMT
< server: uvicorn
< content-length: 15
< content-type: application/json
< 
* Connection #0 to host localhost left intact
{"status":"ok"}
``` 

-  The following is the answer when receiving an invalid request. As you can see here, status code is http `4XX` and some json formatted message.
```bash
$ curl  --verbose -X 'POST'   'http://localhost:8081/v2/vote/'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{  "phone_number": "+8869000000", "question":"QUESTION"}'
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
{"detail":[{"type":"missing","loc":["body","vote"],"msg":"Field required","input":{"phone_number":"+8869000000","question":"QUESTION"},"url":"https://errors.pydantic.dev/2.5/v/missing"}]}

```
# 2. Health check
- Health check is used for monitoring system. The following is the response when receiving a valid request. As you can see here, status code is http `200` (OK) and a json string `{"status":"ok"}`.
```bash
 $ curl -v http://localhost:8081/v1/health-check
*   Trying 127.0.0.1:8081...
* Connected to localhost (127.0.0.1) port 8081 (#0)
> GET /v1/health-check HTTP/1.1
> Host: localhost:8081
> User-Agent: curl/7.78.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< date: Mon, 08 Jan 2024 10:40:44 GMT
< server: uvicorn
< content-length: 15
< content-type: application/json
< 
* Connection #0 to host localhost left intact
{"status":"ok"}
```

```bash
 $ curl -v http://localhost:8081/v2/health-check
*   Trying 127.0.0.1:8081...
* Connected to localhost (127.0.0.1) port 8081 (#0)
> GET /v1/health-check HTTP/1.1
> Host: localhost:8081
> User-Agent: curl/7.78.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< date: Mon, 08 Jan 2024 10:40:44 GMT
< server: uvicorn
< content-length: 15
< content-type: application/json
< 
* Connection #0 to host localhost left intact
{"status":"ok"}
```

# 3. TODO items
- Modify SessionGenerator.py: ideally, we should load db setting from vault. You can search for `TODO` in the code.
- CICD pipeline: we should have a CICD pipeline to build docker image and deploy it to k8s with git actions.
- Put DB in cloud env, e.g. AWS RDS or GCP CloudSQL.
- Put gogobot-log-api image in Dockerhub.
- Prepare YAML files for Kubernetes.
