"""Module contains Task class"""

from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel


class Task(BaseModel, Base):
    """Task class"""
    __tablename__ = 'tasks'
    masterlistdetail_id = Column(String(30),
                                 ForeignKey('masterlistdetails.id'),
                                 nullable=False)
    asign_to = Column(String(20), nullable=False)
    description = Column(String(255), nullable=False)
    due_date = Column(DateTime, nullable=False)
    status_id = Column(String(2), ForeignKey('status.id'), nullable=False)

    masterlistdetail = relationship('MasterListDetail',
                                    backref='task')
    status = relationship('Status', backref='task')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
