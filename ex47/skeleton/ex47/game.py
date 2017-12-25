# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 23:17:07 2017

@author: rimikamajumdar
"""

# Exercise 47: Automated Testing

class Room(object):
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        
    def go(self, direction):
        return self.paths.get(direction, None)
    
    def add_paths(self, paths):
        self.paths.update(paths)