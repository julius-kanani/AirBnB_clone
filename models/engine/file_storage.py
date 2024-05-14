#!/usr/bin/python3
""" file_storage module that supplies the FileStorage class. """
import importlib
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to
    instances.
    """

    classes = {"BaseModel": BaseModel, "User": User, "Place": Place,
               "City": City, "Review": Review, "Amenity": Amenity}
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists).

        If the JSON file exists, loads the objects from the file and adds
        them to __objects dictionary.
        Each object is instantiated based on its class name retrieved from
        the JSON file and added to the dictionary.
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                loaded_objects = json.load(file)
                for key, obj_dict in loaded_objects.items():
                    class_name, obj_id = key.split('.')
                    cls = FileStorage.classes[class_name]
                    obj = cls(**obj_dict)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
