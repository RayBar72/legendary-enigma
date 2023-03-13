#!/usr/bin/env python3
from models.base_model import BaseModel


class User(BaseModel):
    def __init__(self, *args, **kwargs):
        super.__init()
        self.email = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''
