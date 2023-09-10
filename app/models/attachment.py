"""Module contains Task Details class"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel


class Attachment(BaseModel, Base):
    """Task class"""
    __tablename__ = 'attachments'
    task_details_id = Column(String(30), ForeignKey('taskdetails.id'))
    name = Column(String(20), nullable=False)
    description = Column(String(255), nullable=False)
    location = Column(String(20))
    is_research_source = Column(String(5))

    task_details = relationship('TaskDetail', backref='attachment')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
