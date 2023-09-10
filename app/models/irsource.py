"""Module contains IR Source class"""

from sqlalchemy import Column, String
from models.base_model import Base, BaseModel


class IRSource(BaseModel, Base):
    """Ir Source class"""
    __tablename__ = 'irsources'
    name = Column(String(20), unique=True, nullable=False)
    description = Column(String(255), nullable=False)
    symbol = Column(String(2), nullable=False, unique=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
