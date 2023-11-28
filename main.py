import logging
logger = logging.getLogger(__name__)
from datetime import date
import os


from typing import Optional

from fastapi import FastAPI, HTTPException, Request, Response, status
import json
app = FastAPI() 


ENCODEING="utf-8"

@app.post("/save-vote", status_code=status.HTTP_200_OK, response_model=str)
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
