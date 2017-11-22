#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 10:02:29 2017

@author: rimikamajumdar
"""

# Exercise 13: Parameters, Unpacking, Variables
# accepts arguments

# the import is how you add features to your script from the 
# Python feature set
from sys import argv

'''
argv holds the arguments you pass to your Python script when you run it
This line unpacks argv so that the arguments get assigned to four variables
you can work with in order.
'''
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
'''
$ python3.6 ex13.py stuff things that
The script is called: ex13.py
Your first variable is: stuff
Your second variable is: things
Your third variable is: that
'''