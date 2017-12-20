# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 23:12:16 2017

@author: rimikamajumdar
"""

# Exercise 44: Inheritance versus Composition
# Implicit Inheritance
# This file shows implicit inheritance
# These are the implicit actions that happen when the function is defined in
# the parent but not in the child

'''
Inheritance
1. actions on the child imply an action on the parent
2. actions on the child override the action on the parent
3. actions on the child alter the action on the parent
'''

class Parent(object):
    
    def implicit(self):
        print("PARENT implicit()")
        
class Child(Parent):
    # inherits all behavior from Parent
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

'''
Output is the following:
PARENT implicit()
PARENT implicit()
'''