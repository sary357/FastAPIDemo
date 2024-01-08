from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,DateTime
from sqlalchemy import select
from datetime import datetime
from src.v2 import SessionGenerator
import logging

Base = declarative_base()
logger = logging.getLogger(__name__)
class vote(Base):
    __tablename__ = 'votes'
    '''
    phone_number varchar(100) not null,
    query varchar(65535) not null,
    response varchar(65535) not null, 
    vote varchar(100),
    created_at timestamptz not null default current_timestamp,
    vote_at timestamptz,
    '''

    id = Column(Integer, primary_key=True)
    question = Column(String(65535))
    answer = Column(String(65535))
    vote = Column(String(100))
    phone_number = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)
    vote_at = Column(DateTime)


def save_query(user_input_question:str, user_input_answer:str, user_phone:str)->int:
    session = SessionGenerator.sessionGenerator().get_session()
    qa = vote(question=user_input_question, answer=user_input_answer, phone_number=user_phone)
    session.add(qa)
    session.commit()
    qa_id = qa.id
    session.close()
    return qa_id

def save_vote(user_input_question:str, user_phone:str, user_input_answer:str, user_vote:str):
    session = SessionGenerator.sessionGenerator().get_session()
    user_vote_to_update=session.query(vote).filter_by(question=user_input_question, phone_number=user_phone,
                                                       answer=user_input_answer).first()
    if user_vote_to_update:
        user_vote_to_update.vote=user_vote.strip()
        user_vote_to_update.vote_at=datetime.utcnow()
        session.commit()
    else:
        logger.error("Cannot find the query: \""+user_input_question+"\" and phone: \""+user_phone+"\""+ " and answer: \""+user_input_answer+"\"")
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

def health_check()->bool:
    session = SessionGenerator.sessionGenerator().get_session()
    try:
        session.execute(select(1))
        return True
    except Exception as e:
        logger.error("DB is not ready.")
        logger.error("Error in health check: "+str(e))
        return False
    finally:
        session.close()

