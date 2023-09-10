"""Module contains Master class"""

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import backref, relationship
from models.base_model import Base, BaseModel


class MasterList(BaseModel, Base):
    """Master list table class"""
    __tablename__ = 'masterlist'
    raised_by = Column(String(20), nullable=False, unique=True)
    line_manager = Column(String(100), nullable=False)
    priority = Column(String(50), nullable=False, unique=True)
    team_leader = Column(String(20))
    description = Column(String(200), nullable=False)
    main_root_casue = Column(String(50), nullable=False)
    ir_source_id = Column(String(30), ForeignKey('irsources.id'), nullable=False)
    status_id = Column(String(30), ForeignKey('status.id'), nullable=False)

    status = relationship('Status', backref='masterlists')
    ir_source = relationship('IRSource', backref='masterlists')

    def __init__(self, *args, **kwargs):
        """Initialise MasterList"""
        super().__init__(*args, **kwargs)
