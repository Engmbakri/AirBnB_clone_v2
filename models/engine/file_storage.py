#!/usr/bin/python3
"""FileStorage Class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
<<<<<<< HEAD
from models.place import Place
from models.amenity import Amenity
from models.review import Review
=======
from models.amenity import Amenity
from models.review import Review
from models.place import Place
>>>>>>> e0674a08597da2164c53f33d36cbc439bfca69bf

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

class FileStorage:
    """Representation of  an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): Dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

<<<<<<< HEAD
    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects
=======
    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            solo_obj = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    solo_obj[key] = value
            return solo_obj
        else:
            return self.__objects
>>>>>>> e0674a08597da2164c53f33d36cbc439bfca69bf

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
<<<<<<< HEAD
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
=======
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
            for k in temp:
                self.__objects[k] = classes[temp[k]["__class__"]](**temp[k])
        except:
            pass

    def delete(self, obj=None):
        """object remove from objects if it is inside"""
        if obj is not None:
            par = obj.__class__.__name__ + '.' + obj.id
            if par in self.__objects:
                del self.__objects[par]
    def close(self):
        """get reload function"""
        self.reload()
>>>>>>> e0674a08597da2164c53f33d36cbc439bfca69bf
