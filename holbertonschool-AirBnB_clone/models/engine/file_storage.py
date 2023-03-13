#!/usr/bin/env python3
import json
import os.path
from models.base_model import BaseModel
from models.user import User


modelos = {'BaseModel': BaseModel,
           'User': User}


class FileStorage:
    __file_path = 'file.json'
    __objects =  {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        temp = {}
        for k, v in self.__objects.items():
            temp[k] = v.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(temp, f)


    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                r = dict(json.load(f))
                temp = {}
                for k, v in r.items():
                    llave = k.split('.')
                    temp[k] = modelos[llave](**v)
                self.__objects = temp
        else:
            return
