# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 17:38:42 2017

@author: rimikamajumdar
"""

# Exercise 20: Functions and Files

# readine() scans each byte of the file until it finds \n and then returns line
# file is responsible for maintaining current position so each line is read

from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())
    
def rewind(f):
    # seek(0) moves the file to the 0 byte (first byte) in the file
    f.seek(0)
    
def print_a_line(line_count, f):
    # there are empty lines between the lines of the file because
    # the readline() function returns the \n at the end of the line
    # add end = "" to avoid the double spacing between lines
    print(line_count, f.readline(), end = "")
    
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

# current_line is just a variable, no connection to the file at all
current_line = 1
print_a_line(current_line, current_file)

# incrementing current_line
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

# close input file
current_file.close()

'''
Output is the following:
First let's print the whole file:

This is line 1
This is line 2
This is line 3

Now let's rewind, kind of like a tape.
Let's print three lines:
1 This is line 1
2 This is line 2
3 This is line 3
'''