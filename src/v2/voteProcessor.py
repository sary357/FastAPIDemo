from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

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
    created_at = Column(String)