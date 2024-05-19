#!/usr/bin/python3
"""
serialize to to a json file and deseralizes json to instance
"""
import json
import os
#from models.base_model import BaseModel

class FileStorage:
    """
    Serializes adnd deserializes json
    """
    __file_path = "file.json"
    __objects = {}
    
    
    def all(self):
        """
        adds new object to the __objects dict
        """
        return self.__objects
    
    def new(self, obj):
        """
        adds new obj to dict

        Args:
            obj: obj to be added
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
    
    def save(self):
        """
        serializes obj dict to a json file
        """
        from models.base_model import BaseModel
        objdict = {}
        for key, value in self.__objects.items():
            objdict[key] = value.to_dict()
        
        with open(self.__file_path, "w") as file:
            json.dump(objdict, file, indent=2)
            #print("insave")
            #print(obj_dict)
    
    def reload(self):
        """
        deserializes json file to obj dict
        """
        #from models.base_model import BaseModel
        #classlist = {
        #    "BaseModel": BaseModel
        #}
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r') as file:
                    self.__objects = json.load(file)
                    for key, value in self.__objects.items():
                        cls_name, obj_id = key.split('.')
                        from models.base_model import BaseModel
                        cls = BaseModel
                        self.__objects[key] = cls(**value)
                        #if class_name in classlist:
                        #   self.__objects[key] = classlist[class_name](**value)

            except FileNotFoundError:
                pass
        #if os.path.exists(self.__file_path):
        #with open(self.__file_path, 'r') as f:
        #    obj_dict = json.load(f)
        #    for key, value in obj_dict.items():
        #        cls_name, obj_id = key.split('.')
        #        cls = globals()[cls_name]
        #        instance = cls(**value)
        #        self.__objects[key] = instance
