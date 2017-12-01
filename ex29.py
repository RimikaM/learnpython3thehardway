# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 12:00:40 2017

@author: rimikamajumdar
"""

# Exercise 29: What If
# Introduction to if-statement
# try putting boolean expressions in the if-statements

people = 20
cats = 30
dogs = 15


if (people < cats and 1 == 1):
    print("Too many cats! The world is doomed!")

if (people > cats or False):
    print("Not many cats! The world is saved!")
    
if (people < dogs and 3 != 2):
    print("The world is drooled on!")
    
if (people > dogs and (100 == 100 or "Rimika" == "kool")):
    print("The world is dry!")
    
# increment dogs by 5    
dogs += 5

if (people >= dogs or ("Python" == 100)):
    print("People are greater than or equal to dogs.")
    
if (people <= dogs and (not (1 != 1 and 10 == 10))):
    print("People are less than or equal to dogs.")
    
if (people == dogs and (1 == 1 or "5" == str(5))):
    print("People are dogs.")
    
'''
Output is the following:
Too many cats! The world is doomed!
The world is dry!
People are greater than or equal to dogs.
People are less than or equal to dogs.
People are dogs.
'''