#!/usr/bin/pyhton3
"""This module defines a class `user`"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage_t
import models


class User(BaseModel, Base):
    '''Defines a user'''
    if models.storage_t == 'db':
        __tablename__ = 'users'

        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user", cascade="all, delete-orphan")

    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __str__(self):
        """Return the string representation of the object."""
        state_dict = self.__dict__.copy()
        # Remove the '_sa_instance_state' attribute
        state_dict.pop('_sa_instance_state', None)
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, state_dict)

