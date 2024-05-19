#!/usr/bin/python3
"""
comments on class
"""
import uuid
from datetime import datetime
import time

class BaseModel:
    """
    BaseModel class
    """
    def __init__(self, *args, **kwargs):
        """
        init method
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
     
    def __str__(self):
        """
        str method
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """
        save method
        """
        self.updated_at = datetime.now()
        self.__dict__.update({"updated_at": datetime.now()})
        
    def to_dict(self):
        """
        returns a dict rep od instances
        """
        master_dict = self.__dict__
        master_dict.update({"__class__": self.__class__.__name__,
                            "id": self.id,
                            "created_at": self.created_at.isoformat(),
                            "updated_at": self.updated_at.isoformat()})
        return master_dict
    
model = BaseModel()
# model.save()
# print(model)
# 
# time.sleep(5)
# print("\n after sleep")
# 
# model.save()
# print(model)
# 
# json_repr = model.to_dict()
# print("\n json repr")
# print(json_repr)
# print(type(json_repr["created_at"]))
# print(type(json_repr["updated_at"]))

