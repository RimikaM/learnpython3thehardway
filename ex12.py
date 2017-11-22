#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 23:29:07 2017

@author: rimikamajumdar
"""

# Exercise 12: Prompting People

# prompts the user with "Name?" and prints a space for the user to answer and 
# puts the result into the variable y
y = input("Name? ")
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy")