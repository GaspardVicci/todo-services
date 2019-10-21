from uuid import uuid4

from sqlalchemy import Column, Date, DateTime, Integer, String, Table, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base


def randkey():
    return str(uuid4())

Base = declarative_base()

class Model(Base):
    """Global schema"""
    __abstract__ = True
    id = Column(String(80), primary_key=True, default=randkey, nullable=False)
    _created = Column(DateTime, default=func.now(), nullable=False)
    _updated = Column( DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    _etag = Column(String(40))

class Tasks(Model):
    """Schema for the tasks"""
    __tablename__ = 'tasks'
    name = Column(String(80))
    status = Column(String(120))
    def __init__(self, name, status, **kwargs):
        super(Tasks).__init__()
        self.name = name
        self.status = status
