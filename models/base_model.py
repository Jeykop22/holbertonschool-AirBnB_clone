#!/usr/bin/python3
"""Write a class BaseModel that defines all common attributes/methods
for other classes"""
import uuid
from datetime import datetime


class BaseModel:
    """Write a class BaseModel that defines all common attributes/methods
    for other classes"""
    def __init__(self, *args, **kwargs):
        """Initializes BaseModel instance"""
        if not kwargs or len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

        else:
            for key, value in kwargs.items():
                if key == "created_at":
                    value = datetime.fromisoformat(value)
                elif key == "updated_at":
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """Returns a readable string representation of an instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance, datetime in iso format"""
        dictionary = {"__class__": self.__class__.__name__}
        for key, value in self.__dict__.items():
            if key == "created_at":
                dictionary[key] = value.isoformat()
            elif key == "updated_at":
                dictionary[key] = value.isoformat()
            else:
                dictionary[key] = value
        return dictionary
