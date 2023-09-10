"""Module contains Base Model class"""
from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """BaseModel class"""
    id = Column(String(60), primary_key=True)
    date_created_on = Column(DateTime,
                             default=datetime.utcnow(),
                             nullable=False)
    date_updated_on = Column(DateTime,
                             default=datetime.utcnow(),
                             onupdate=datetime.utcnow(),
                             nullable=False)
    status_id = Column(String(20))

    def __init__(self, *args, **kwargs):
        """Initialisation of base model class"""
        self.id = str(uuid4())
        self.date_created_on = datetime.utcnow()
        self.date_updated_on = self.date_created_on
