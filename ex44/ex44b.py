# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 21:30:29 2017

@author: rimikamajumdar
"""

# Exercise 44: Inheritance versus Composition
# Inheritance: Override Explicitly

class Parent(object):
    
    def override(self):
        print("PARENT override()")
        
class Child(Parent):
    
    # if you want the child to behave differently, define a function with the
    # same name override and replace the functionality
    def override(self):
        print("CHILD override()")
        
dad = Parent()
son = Child()

dad.override()
son.override()

'''
Output is the following:
PARENT override()
CHILD override()
'''