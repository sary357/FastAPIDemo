import logging
logger = logging.getLogger(__name__)
from datetime import date
import os
from pydantic import BaseModel

from typing import Optional

from fastapi import FastAPI, HTTPException, Request, Response, status
import json
from src.v2 import voteProcessor
from src.v2 import SessionGenerator
app = FastAPI() 


ENCODEING="utf-8"

# Class 1: Vote
# field: id(int), phone_number (str), query(str), response(str), vote(str)
# Class 2: QA
# field: phone_number (str), query(str), response(str)

class Vote(BaseModel):
    id: Optional[int] = None
    phone_number: Optional[str] = None
    query: Optional[str] = None
    vote: str

class QA(BaseModel):
    phone_number: str
    query: str
    response: str

@app.post("/v2/vote/")
async def save_vote(vote: Vote):
    logger.info('Got 1 vote: %s', vote)
    if vote.id:
        voteProcessor.save_vote_by_id(id=vote.id, user_vote=vote.vote)
    else:
        voteProcessor.save_vote(user_query=vote.query, user_phone=vote.phone_number, user_vote=vote.vote)
    return {"status": "ok"}

@app.post("/v2/qa/")
async def save_query(qa: QA):
    logger.info('Got 1 QA: %s', qa)
    id=voteProcessor.save_query(user_query=qa.query, user_response=qa.response, user_phone=qa.phone_number)
    return {"id":id, "status": "ok"}

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