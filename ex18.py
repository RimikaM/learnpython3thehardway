# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 16:55:48 2017

@author: rimikamajumdar
"""

# Exercise 18: Names, Variables, Code, Functions

# this one is like your scripts with argv
# *args tells Python to take all the arguments in a function and put
# them in args as a list. It's like argv, but for functions.
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
    
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
    
# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments    
def print_none():
    print("I got nothin'.")
    
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

'''
Output is the following:
arg1: Zed, arg2: Shaw
arg1: Zed, arg2: Shaw
arg1: First!
I got nothin'.
'''