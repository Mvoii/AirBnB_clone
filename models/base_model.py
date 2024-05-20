#!/usr/bin/python3
"""
comments on class
"""
import uuid
from datetime import datetime
#from .__init__ import storage

class BaseModel:
    """
    BaseModel class
    """
    def __init__(self, *args, **kwargs):
        """
        init method
        """
        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"] and type(value) == str:
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from .__init__ import storage
            storage.new(self)
     
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
        from .__init__ import storage
        storage.new(self)
        storage.save()
        
    def to_dict(self):
        """
        returns a dict rep od instances
        """
        master_dict = self.__dict__.copy()
        master_dict.update({'__class__': self.__class__.__name__,
                            'id': self.id,
                            'created_at': self.created_at.isoformat(),
                            'updated_at': self.updated_at.isoformat()})
        return master_dict
