from sqlalchemy import Column, Date, DateTime, Integer, String, Table, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Model(Base):
    __abstract__ = True
    _created = Column(DateTime, default=func.now(), nullable=False)
    _updated = Column( DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    _etag = Column(String(40))

class Tasks(Model):
    """"""
    __tablename__ = 'tasks'
    name = Column(String(80), primary_key=True)
    status = Column(String(120))
    def __init__(self, name, status):
        super(Tasks).__init__()
        self.name = name
        self.status = status
