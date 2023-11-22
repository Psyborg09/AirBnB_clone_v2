#!/usr/bin/python3
"""This module create the class FileStorage"""
import json


class FileStorage():
    '''serializes instances to a JSON file and deserializes
       JSON file to instances
    '''
    __file_path = "file.json"
    __objects = {}
    
    def all(self, cls=None):
        '''returns the dict `__objects`'''
        if cls:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        else:
            return self.__objects


    def new(self, obj):
        '''sets in `__objects` the `obj` with key `<obj class name>.id`'''
        name = obj.__class__.__name__
        key = f'{name}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        '''serializes `__objects` to the JSON file'''
        with open(self.__file_path, 'w') as file:
            dict_rep = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(dict_rep, file)

    def reload(self):
        '''deserializes the JSON file to `__objects`'''
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                new_obj = json.load(file)
                for value in new_obj.values():
                    loaded_object = eval(value["__class__"])(**value)
                    self.new(loaded_object)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
