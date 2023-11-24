#!/usr/bin/python3
"""This module defines a class `State`"""

from models.base_model import BaseModel
import models

class State(BaseModel):
    '''Defines a State'''
    def __init__(self, *args, **kwargs):
        if 'name' in kwargs:
            self.name = kwargs['name']
        else:
            self.name = ""
        super().__init__(*args, **kwargs)
