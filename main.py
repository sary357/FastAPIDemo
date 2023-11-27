import logging
logger = logging.getLogger(__name__)
from datetime import date
import os


from typing import Optional

from fastapi import FastAPI, Request, Response, status

app = FastAPI() 

ENCODEING="utf-8"

@app.post("/save-vote", status_code=status.HTTP_200_OK)
async def save_vote(req:Request,res:Response):
    c=await req.body()
    if is_valid_request_body(c):
        c=c.decode(ENCODEING)
        logger.info(c.replace("\n",""))
        return
    res.status_code = status.HTTP_400_BAD_REQUEST
        

def is_valid_request_body(body) -> bool:
    if body is None:
        return False
    if len(body) <=1:
        return False  
    return True
