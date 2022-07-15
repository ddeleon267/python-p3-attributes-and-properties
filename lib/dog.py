#!/usr/bin/env python3
import ipdb

class Dog:
    def __init__(self, name=""):
        self._name = ""
        
    def get_name(self):
        return self._name

    def set_name(self, name):
        # ipdb.set_trace()

        if type(name) == "str" and len(name) > 0:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    
    name = property(get_name, set_name)