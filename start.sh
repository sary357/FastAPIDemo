#!/bin/sh

# Start Gunicorn processes
# port: 8081
uvicorn --port 8081  main:app --host 0.0.0.0 --log-config conf/logging.conf
