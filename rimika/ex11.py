#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 23:16:19 2017

@author: rimikamajumdar
"""

# Exercise 11: Asking Questions

# end = ' ' at the end of each print line tells print not to end
# the line with a new line character and go to the next line
print("How old are you?", end = ' ')
age = input()
print("How tall are you?", end = ' ')
height = input()
print("How much do you weigh?", end = ' ')
weight = input()

print(f"So, you\'re {age} old, {height} tall and {weight} heavy.")

# x = int(input()) gets the number as a string from input(), then
# converts it to an integer using int()