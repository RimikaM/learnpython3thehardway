# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 14:08:21 2017

@author: rimikamajumdar
"""

# Exercise 15: Reading Files

from sys import argv

script, filename = argv

# used argv to ask the user what file to open
# open() makes something called a file object
txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())
# close file after reading
txt.close()

print("Type the filename again:")
file_again = input("> ")

# used input() to ask user what file to open
txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
'''
Output is the following:
Here's your file ex15_sample.txt:
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.
Type the filename again:
> ex15_sample.txt
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.
'''