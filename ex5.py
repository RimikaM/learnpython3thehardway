#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 11:04:11 2017

@author: rimikamajumdar
"""

# Exercise 5: More variables and printing

name = 'Zed A. Shaw'
age = 35
height = 74 * 2.54 #inches to centimeters
weight = 180 * 0.453592 #pounds to kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

'''
string = f"Hello {some_variable}"
f is for format
the variable you want to print goes inside {}
string2 = "Hello {}"
print(string2.format(some_variable))
'''

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")
print("some numbers {} {} {}".format(age, height, weight))
print("blah blah {}".format(name))
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# Example
