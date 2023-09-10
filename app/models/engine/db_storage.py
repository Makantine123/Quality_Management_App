"""Module conatins DBStorage Class"""
import os

from models.base_model import Base

from models.attachment import Attachment
from models.irsource import IRSource
from models.masterdetail import MasterListDetail
from models.masterlist import MasterList
from models.revision import Revision
from models.status import Status
from models.task import Task
from models.taskdetail import TaskDetail
from models.user import User

from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_path = os.path.join(
    os.path.abspath(
        os.path.dirname(__file__)), "../../data", "database.db")

classes = {"Attachment": Attachment, "IRSource": IRSource, "MasterList": MasterList,
           "MasterListDetail": MasterListDetail, "Revision": Revision,
           "Status": Status, "Task": Task, "TaskDetail": TaskDetail,
           "User": User}


class DBStorage:
    """Database engine"""
    __engine = None
    __sessiion = None

    def __init__(self):
        """Initialisation of instance"""
        self.__engine = create_engine(f'sqlite:///{db_path}')
        self.pub_session = None

    def new(self, obj):
        """Add object to database"""
        self.__session.add(obj)

    def save(self):
        """Save method for database"""
        self.__session.commit()

    def delete(self, obj):
        """Deletes a object from database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session()

    def close(self):
        """Closes session"""
        if self.__sessiion is not None:
            self.__sessiion.remove()

    def query_db(self, cls):
        """Query the database"""
        return self.__session.query(cls)
