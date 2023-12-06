import logging
logger = logging.getLogger(__name__)
from datetime import date
import os
from pydantic import BaseModel

from typing import Optional

from fastapi import FastAPI, HTTPException, Request, Response, status
import json
app = FastAPI() 


ENCODEING="utf-8"

# Class 1: Vote
# field: phone_number (str), query(str), response(str), vote(str)
# Class 2: QA
# field: phone_number (str), query(str), response(str)
class Vote(BaseModel):
    phone_number: str
    query: str
    vote: str

class QA(BaseModel):
    phone_number: str
    query: str
    response: str

@app.post("/v1/vote/")
async def save_vote(vote: Vote):
    logger.info(vote)
    return {"status": "ok"}

@app.post("/v1/qa/")
async def save_query(qa: QA):
    logger.info(qa)
    return {"status": "ok"}

def is_valid_request_body(body) -> bool:
    if body is None:
        return False
    try:
        content=json.loads(body)
        if content is None or len(content)==0:
            return False
    except Exception as e:
        logger.error("Invalid user input [Incorrect JSON format]: "+body)
        logger.error(e)
        return False
    
    return True

@app.get("/healthcheck")
async def health_check():
    return {"status": "ok"}