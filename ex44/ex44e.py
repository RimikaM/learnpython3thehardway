# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 00:03:46 2017

@author: rimikamajumdar
"""

# Exercise 44: Inheritance versus Composition
# Composition
# Inheritance is useful but another way to do the exact same thing is to just
# use other classes and modules

class Other(object):
    
    def override(self):
        print("OTHER override()")
        
    def implicit(self):
        print("OTHER implicit()")
        
    def altered(self):
        print("OTHER altered()")
        
class Child(object):
    
    def __init__(self):
        self.other = Other()
        
    def implicit(self):
        self.other.implicit()
        
    def override(self):
        print("CHILD override()")
        
    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")
        
son = Child()

son.implicit()
son.override()
son.altered()

'''
Output is the following:
OTHER implicit()
CHILD override()
CHILD, BEFORE OTHER altered()
OTHER altered()
CHILD, AFTER OTHER altered()
'''