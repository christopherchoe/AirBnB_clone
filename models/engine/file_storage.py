#!/usr/bin/python3
"""
    Module containing the ``FileStorage`` class.
"""
import json


class FileStorage:
    """
        The ``FileStorage`` class.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
            Returns the class `__objects` variable.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
            Adds a key/value pair to class `__objects` variable.

            Args:
                obj: (:obj:`BaseModel`): A `BaseModel` instance.
        """
        FileStorage.__objects[obj.__class__.__name__ + '.' + obj.id] = obj.to_dict()

    def save(self):
        """
            Serializes `__object` to the JSON file specified by `__file_path`.
        """
        try:
            with open(FileStorage.__file_path, 'w') as f:
                json.dump(FileStorage.__objects, f)
        except IOError:
            pass

    def reload(self):
        """
            Deserialize the JSON file specified by `__file_path` to `__objects`
            .
        """
        try:
            with open('file.json', 'r') as f:
                FileStorage.__objects = json.load(f)
        except IOError:
            pass
