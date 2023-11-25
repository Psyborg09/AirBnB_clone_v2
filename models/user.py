#!/usr/bin/pyhton3
"""This module defines a class `user`"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    '''Defines a user'''
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    def __str__(self):
        """Return the string representation of the object."""
        state_dict = self.__dict__.copy()
        # Remove the '_sa_instance_state' attribute
        state_dict.pop('_sa_instance_state', None)
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, state_dict)

