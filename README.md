# FastAPIDemo
## 1. Project Introduction
This project is used to save all input into a file as long as it is a POST request.

## 2. Folder Structure
```
├── README.md: Introduction
├── main.py: main file
├── start.sh: the script to start the project
├── test_main.py: test file
├── requirements.txt
├── conf
|   └── logging.conf: logging configuration file
├── scripts
|   └── process_log.py: extract user input from the log file
└── logs
    └── access.log: log file
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
$ uvicorn --port 8081  main:app --reload --log-config conf/logging.conf
```

- Then, you can access the API by http://localhost:8081/save-vote. You can test it with the command `curl`. The following is the response when receiving a valid request. As you can see here, status code is http `200` (OK) and `null` body.

```bash
$ curl --verbose -X POST http://localhost:8081/save-vote -d '{"key1":"value1", "key2":"value2}'
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1:8081...
* Connected to localhost (127.0.0.1) port 8081 (#0)
> POST /save-vote HTTP/1.1
> Host: localhost:8081
> User-Agent: curl/7.78.0
> Accept: */*
> Content-Length: 33
> Content-Type: application/x-www-form-urlencoded
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< date: Mon, 27 Nov 2023 07:26:40 GMT
< server: uvicorn
< content-length: 4
< content-type: application/json
< 
* Connection #0 to host localhost left intact

``` 

-  The following is the response when receiving an invalid request. As you can see here, status code is http `400` (Bad Request) and `null` body.
```bash
$ curl --verbose -X POST http://localhost:8081/save-vote -d ''
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1:8081...
* Connected to localhost (127.0.0.1) port 8081 (#0)
> POST /save-vote HTTP/1.1
> Host: localhost:8081
> User-Agent: curl/7.78.0
> Accept: */*
> Content-Length: 0
> Content-Type: application/x-www-form-urlencoded
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 400 Bad Request
< date: Mon, 27 Nov 2023 07:28:59 GMT
< server: uvicorn
< content-length: 4
< content-type: application/json
< 
* Connection #0 to host localhost left intact

```


### 3.2 Test it
- You don't need to start anything. Just run the following command.
```python
$ python test_main.py

```

### 3.3 get user's ouput
- All of access log including user's inpurt will be saved in log/access.log, you can get user's output by the following command.
```python
$ python scripts/process_log.py log/access.log log/user_input.log
```
- After running the command, you can see the user's input in the file `log/user_input.log`.
- Note: The log file `log/access.log` will be rotated every day. The old log file will be saved as `log/access.log.YYYY-MM-DD`.
