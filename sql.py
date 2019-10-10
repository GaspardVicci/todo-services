from sqlalchemy import Column, String, Integer, Date, Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Tasks(Base):
    """"""
    __tablename__ = 'tasks'
    name = Column(String(80), primary_key=True)
    status = Column(String(120))

    def __init__(self, _updated, _created, _etag, name, status):
        self.name = name
        self.status = status
