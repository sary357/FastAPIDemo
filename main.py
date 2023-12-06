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

@app.post("/v2/vote/")
async def save_vote(vote: Vote):
    logger.info(vote)
    return {"status": "ok"}

@app.post("/v2/qa/")
async def save_query(qa: QA):
    logger.info(qa)
    return {"status": "ok"}

@app.get("/v2/healthcheck")
async def health_check():
    return {"status": "ok"}

@app.post("/v1/save-vote", status_code=status.HTTP_200_OK, response_model=str)
async def save_vote(req:Request,res:Response):
    c=await req.body()
    try:
        decoded_content=c.decode(ENCODEING)
        if is_valid_request_body(decoded_content):
            logger.critical(decoded_content.replace("\n",""))
            return ""
    except Exception as e:
        logger.error("Invalid user input: "+c)
        logger.error(e)
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid request body")

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

@app.get("/v1/health-check", status_code=status.HTTP_200_OK, response_model=dict)
async def health_check():
    return {"status": "ok"}