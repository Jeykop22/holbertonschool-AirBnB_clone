#!/usr/bin/python3
"""This modules defines the hightest parent class (BaseModel)"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """This class represent a model for the futures instances of this one"""

    def __init__(self, *args, **kwargs):
        """Constructor of the class, used to create or recreate an instance
"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for (key, value) in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        """Return a string that describes the current instance."""
        class_name = self.__class__.__name__
        return (f"[{class_name}] ({self.id}) {self.__dict__}")

    def save(self):
        """Update the date/time attribute (updated_at)."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dict that represents the current instance."""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict