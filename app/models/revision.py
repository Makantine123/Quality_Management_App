"""Module contains Task Details class"""

from sqlalchemy import Column, DateTime, String, ForeignKey
from models.base_model import Base, BaseModel


class Revision(BaseModel, Base):
    """Revision class"""
    __tablename__ = 'revisions'
    master_list_id = Column(String(30),
                            ForeignKey('masterlist.id'),
                            nullable=False)
    requested_by = Column(String(20), nullable=False)
    approved_by = Column(String(20), nullable=False)
    reason_for_revision = Column(String(255), nullable=False)
    revised_date = Column(DateTime, nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
