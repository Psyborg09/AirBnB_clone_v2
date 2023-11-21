#!/usr/bin/python3
"""This Module creates the class named BaseModel"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if (key == 'created_at') or (key == 'updated_at'):
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """prints an instance of the object specified"""
        className = self.__class__.__name__
        selfId = self.id
        selfDict = self.__dict__

        return "[{}] ({}) {}".format(className, selfId, selfDict)

    def save(self):
        """updates the 'updated_at' attribute with current datetime"""
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the __dict__
           of the instance
        """
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({"__class__": self.__class__.__name__})
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()

        return dictionary
