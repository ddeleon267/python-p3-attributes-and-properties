#!/usr/bin/env python3
import ipdb

class Dog:
    breeds = [
        "Mastiff",
        "Chihuahua",
        "Corgi",
        "Shar pei",
        "Beagle",
        "French Bulldog",
        "Pug",
        
    ]

    def __init__(self):
        self._name = ""
        self._breed = ""
        
    def get_name(self):
        return self._name

    def set_name(self, name):
     
        if type(name) == str and len(name) > 0 and len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
    
    def get_breed(self):
        return self._breed

    def set_breed(self, breed):

        if breed in self.breeds:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    
    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)