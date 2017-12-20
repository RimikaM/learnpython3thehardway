# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 16:25:26 2017

@author: rimikamajumdar
"""

# Exercise 44: Inheritance versus Composition
# Inheritance: Alter Before or After
# want to alter the behavior before or after the parent class's version runs

class Parent(object):
    
    def altered(self):
        print("PARENT altered()")
        
class Child(Parent):
    
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        # use super to get the Paret.altered() function run
        # call super with arguments Child and self, then call altered()
        super(Child, self).altered()
        # now Child.altered() function continues to print out the after message
        print("CHILD, AFTER PARENT altered()")
        
dad = Parent()
son = Child()

dad.altered()
son.altered()

'''
Output is the following:
PARENT altered()
CHILD, BEFORE PARENT altered()
PARENT altered()
CHILD, AFTER PARENT altered()
'''