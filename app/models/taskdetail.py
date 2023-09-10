"""Module contains Task Details class"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel


class TaskDetail(BaseModel, Base):
    """Task class"""
    __tablename__ = 'taskdetails'
    task_id = Column(String(30), ForeignKey('tasks.id'))
    details = Column(String(255), nullable=False)
    attachment_name = Column(String(20), nullable=False)
    saved = Column(String(20), nullable=False)

    task = relationship('Task', backref='taskdetail')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
