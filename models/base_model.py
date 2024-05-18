#!/usr/bin/python3

"""
Write a class BaseModel that defines all common attributes/methods for other classes:

    models/base_model.py
    Public instance attributes:
        id: string - assign with an uuid when an instance is created:
            you can use uuid.uuid4() to generate unique id but don't forget to convert to a string
            the goal is to have unique id for each BaseModel
        created_at: datetime - assign with the current datetime when an instance is created
        updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
    __str__: should print: [<class name>] (<self.id>) <self.__dict__>
    Public instance methods:
        save(self): updates the public instance attribute updated_at with the current datetime
        to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance:
            by using self.__dict__, only instance attributes set will be returned
            a key __class__ must be added to this dictionary with the class name of the object
            created_at and updated_at must be converted to string object in ISO format:
                format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
                you can use isoformat() of datetime object
            This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our BaseModel
"""

import json
from uuid import uuid4
from datetime import date, datetime
import time

class BaseModel:
    """Super class fro all"""
    def __init__(self) -> None:
        self.id = str(uuid4())
        self.created_at = datetime.now()#.strftime("%Y-%m-%dT%H:%M:%S")
        self.updated_at = self.created_at
        
    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """sets updated_at to current datetime"""
        self.updated_at = datetime.now()#.strftime("%Y-%m-%dT%H:%M:%S")
        
    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        master_dict = self.__dict__
        
        master_dict["created_at"] = master_dict["created_at"].isoformat() # self.created_at.isoformat()
        master_dict["updated_at"] = master_dict["updated_at"].isoformat() # self.updated_at.isoformat()
        master_dict["__class__"] = self.__class__.__name__
        return master_dict

model = BaseModel()
print(model)
time.sleep(10)
model.save()
print("\n")
print(model)
print(type(model.created_at))
print(type(model.updated_at))

json_repr = model.to_dict()

print("\n")
print(json_repr)
print(type(json_repr["created_at"]))
print(type(json_repr["updated_at"]))
