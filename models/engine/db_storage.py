#!/usr/bin/python3
"""
Contains the class DBStorage
"""

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from os import environ
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import BaseModel, Base

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the DBStorage instance"""
        HBNB_MYSQL_USER = environ.get("HBNB_MYSQL_USER")
        HBNB_MYSQL_PWD = environ.get("HBNB_MYSQL_PWD")
        HBNB_MYSQL_HOST = environ.get("HBNB_MYSQL_HOST")
        HBNB_MYSQL_DB = environ.get("HBNB_MYSQL_DB")
        HBNB_ENV = environ.get("HBNB_ENV")


        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))

        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

    def all(self, cls=None):
        """Query all objects of a given class"""
        results = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objects = self.__session.query(classes[clss]).all()
                for obj in objects:
                    key = obj.__class__.__name__ + '.' + obj.id
                    results[key] = obj
        return results

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete the object from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables and recreate the current database session"""
        s_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(s_factory)
        self.__session = Session

