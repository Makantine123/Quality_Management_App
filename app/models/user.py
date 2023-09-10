"""Module contains user class"""

from sqlalchemy import Column, String
from models.base_model import Base, BaseModel
from flask_login import UserMixin


class User(BaseModel, UserMixin, Base):
    """User class"""
    __tablename__ = 'users'
    username = Column(String(20), nullable=False, unique=True)
    password_hsh = Column(String(100), nullable=False)
    email = Column(String(50), nullable=False, unique=True)

    def __init__(self, *args, **kwargs):
        """Initialise User"""
        super().__init__(*args, **kwargs)
