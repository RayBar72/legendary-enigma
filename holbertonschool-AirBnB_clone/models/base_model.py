#!/usr/bin/env python3
import uuid
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.updated_at = self.created_at = datetime.now()
            models.storage.new(self)

        else:
            for k in kwargs.keys():
                if k == '__class__':
                    pass
                elif k == 'created_at' or k == 'updated_at':
                    setattr(self, k, datetime.strptime(kwargs[k], '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, k, kwargs[k])

    def __str__(self):
        name = self.__class__.__name__
        id = self.id
        dicto = self.__dict__
        return '[{}] ({}) {}'.format(name, id, dicto)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dicto = self.__dict__.copy()
        dicto['__class__'] = self.__class__.__name__
        dicto['created_at'] = self.created_at.isoformat()
        dicto['updated_at'] = self.updated_at.isoformat()
        return dicto
