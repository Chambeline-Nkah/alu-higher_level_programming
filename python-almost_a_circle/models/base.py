#!/usr/bin/python3
"""Creating an empty class called Base"""


import json


class Base:
    """Creating class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Function with an id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
