from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,DateTime
from sqlalchemy import select
from datetime import datetime
from src.v2 import SessionGenerator
from sqlalchemy.orm.exc import NoResultFound
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
    qa = vote(question=user_input_question, answer=user_input_answer, phone_number=user_phone)
    session = SessionGenerator.sessionGenerator().get_session()
    try:
        session.add(qa)
        session.commit()
        qa_id = qa.id
        return qa_id
    except Exception as e:
        logger.error(e.__class__.__name__)
        logger.error("Error in save_query: "+str(e))
        return -1
    finally:
        session.close()

def save_vote(user_input_question:str, user_phone:str, user_input_answer:str, user_vote:str)-> bool:
    session = SessionGenerator.sessionGenerator().get_session()
    try:
        # I tried to use with_for_share() but it does not work
        # .first() -> in this case, there could be more that 1 result, I will get the latest one
        user_vote_to_updates=session.query(vote).filter_by(question=user_input_question, phone_number=user_phone,
                                                        answer=user_input_answer).with_for_update()
        if user_vote_to_updates and len(user_vote_to_updates.all()) > 0:
            user_vote_to_update=user_vote_to_updates.order_by(vote.created_at.desc()).first()
            user_vote_to_update.vote=user_vote.strip()
            user_vote_to_update.vote_at=datetime.utcnow()
            session.commit()
            return True
        else:
            logger.error("Cannot find the question: \""+str(user_input_question)+"\"/answer: \""+str(user_input_answer)+"\"/phone: \""+str(user_phone)+"\"")
            return True
    except Exception as e:
        logger.error(e.__class__.__name__)
        logger.error("Error in save_vote: "+str(e))
        return False
    finally:
        session.close()


def save_vote_by_id(id:int, user_vote:str)-> bool:
    session = SessionGenerator.sessionGenerator().get_session()
    try:
        user_vote_to_update=session.query(vote).filter_by(id=id).with_for_update().one()
        user_vote_to_update.vote=user_vote.strip()
        user_vote_to_update.vote_at=datetime.utcnow()
        session.commit()
        return True
    except NoResultFound as e:
        logger.error("Cannot find the id: \""+str(id)+"\"")
        return True
    except Exception as e:
        logger.error(e.__class__.__name__)
        logger.error("Error in save_vote_by_id: "+str(e))
        return False
    finally:
        session.close() 

def health_check()->bool:
    session = SessionGenerator.sessionGenerator().get_session()
    try:
        session.execute(select(1))
        return True
    except Exception as e:
        logger.error("Error in health check: "+str(e))
        return False
    finally:
        session.close()


