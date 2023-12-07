from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,DateTime
from datetime import datetime
from src.v2 import SessionGenerator
import logging

Base = declarative_base()
logger = logging.getLogger(__name__)
class vote(Base):
    __tablename__ = 'votes'
    '''
    phone varchar(100) not null,
    query varchar(65535) not null,
    response varchar(65535), 
    vote varchar(100),
    created_at timestamptz not null default current_timestamp,
    vote_at timestamptz,
    '''

    id = Column(Integer, primary_key=True)
    query = Column(String(65535))
    response = Column(String(65535))
    vote = Column(String(100))
    phone = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)
    vote_at = Column(DateTime)


def save_query(user_query:str, user_response:str, user_phone:str)->int:
    session = SessionGenerator.sessionGenerator().get_session()
    qa = vote(query=user_query.strip(), response=user_response.strip(), phone=user_phone.strip())
    session.add(qa)
    session.commit()
    qa_id = qa.id
    session.close()
    return qa_id

def save_vote(user_query:str, user_phone:str, user_vote:str):
    session = SessionGenerator.sessionGenerator().get_session()
    user_vote_to_update=session.query(vote).filter_by(query=user_query.strip(), phone=user_phone.strip()).first()
    if user_vote_to_update:
        user_vote_to_update.vote=user_vote.strip()
        user_vote_to_update.vote_at=datetime.utcnow()
        session.commit()
    else:
        logger.error("Cannot find the query: \""+user_query+"\" and phone: \""+user_phone+"\"")
    session.close()

def save_vote_by_id(id:int, user_vote:str):
    session = SessionGenerator.sessionGenerator().get_session()
    user_vote_to_update=session.query(vote).filter_by(id=id).first()
    if user_vote_to_update:
        user_vote_to_update.vote=user_vote.strip()
        user_vote_to_update.vote_at=datetime.utcnow()
        session.commit()
    else:
        logger.error("Cannot find the id: \""+str(id)+"\"")
    session.close()