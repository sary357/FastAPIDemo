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
    question: Optional[str] = None
    answer: Optional[str] = None
    vote: str

class QA(BaseModel):
    phone_number: str
    question: str
    answer: str

@app.post("/v2/vote/")
async def save_vote(vote: Vote):
    logger.info('Got 1 vote: %s', vote)
    if vote.id:
        voteProcessor.save_vote_by_id(id=vote.id, user_vote=vote.vote)
    elif vote.question and vote.phone_number and vote.answer:
        voteProcessor.save_vote(user_input_question=vote.question, user_phone=vote.phone_number, 
                                user_vote=vote.vote, user_input_answer=vote.answer)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid request body: missing id or (phone_number + question + response)")
    return {"status": "ok"}

@app.post("/v2/qa/")
async def save_query(qa: QA):
    logger.info('Got 1 Question/Answer: %s', qa)
    id=voteProcessor.save_query(user_input_question=qa.question, user_input_answer=qa.answer, user_phone=qa.phone_number)
    return {"id":id, "status": "ok"}

@app.get("/v2/healthcheck")
async def health_check():
    return {"status": "ok"}

@app.get("/v1/health-check")
async def health_check():
    return {"status": "ok"}