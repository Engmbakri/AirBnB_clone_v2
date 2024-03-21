#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class FileStorage:
    """ s class seriali and
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """ Returns a dictionary of __object"""
        mdic = {}
        if cls:
            dictionary = self.__objects
            for k in dictionary:
                partition = k.replace('.', ' ')
                partition = shlex.split(partition)
                if (partition[0] == cls.__name__):
                    mdic[k] = self.__objects[k]
            return (mdic)
        else:
            return self.__objects

    def new(self, obj):
        """ object to known """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        dic = {}
        for k, v in self.__objects.items():
            dic[k] = v.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(dic, f)

    def reload(self):
        """Path JSON """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ element vanion"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """ Function reload("""
        self.reload()
