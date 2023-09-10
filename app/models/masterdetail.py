"""Module contains Master List details class"""

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel


class MasterListDetail(BaseModel, Base):
    """Master List Details class"""
    __tablename__ = 'masterlistdetails'
    master_list_id = Column(Integer, ForeignKey('masterlist.id'))
    main_causes = Column(String(255), nullable=False)
    steps_required = Column(String(255), nullable=False)
    by_who = Column(String(255), nullable=False)
    due_date = Column(DateTime, nullable=False)
    date_completed = Column(DateTime)
    status_id = Column(String(30), ForeignKey('status.id'))

    status = relationship('Status', backref='masterlistdetail')
    masterlist = relationship('MasterList', backref='masterlistdetail')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
