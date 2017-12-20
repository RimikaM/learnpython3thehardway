# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 16:33:47 2017

@author: rimikamajumdar
"""

# Exercise 44: Inheritance versus Composition
# Inheritance: All Three Combined
# this file shows each kind of interaction from inheritance

class Parent(object):
    
    def override(self):
        print("PARENT override()")
        
    def implicit(self):
        print("PARENT implicit()")
        
    def altered(self):
        print("PARENT altered()")
        
class Child(Parent):
    
    def override(self):
        print("CHILD override()")
        
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")
        
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

'''
Output is the following:
PARENT implicit()
PARENT implicit()
PARENT override()
CHILD override()
PARENT altered()
CHILD, BEFORE PARENT altered()
PARENT altered()
CHILD, AFTER PARENT altered()
'''