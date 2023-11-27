#!/bin/sh

# Start Gunicorn processes
# port: 8081
uvicorn --port 8081  main:app --reload --log-config conf/logging.conf
