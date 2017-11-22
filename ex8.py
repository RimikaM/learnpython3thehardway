#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 11:38:24 2017

@author: rimikamajumdar
"""

# Exercise 8: Printing, Printing

formatter = "{} {} {} {}"

''' 
pass to format four arguments, which match up to the four {}s in the 
formatter variable. This is like passing arguments to the command line 
command format
'''

# prints 4 numbers with spaces in between
print (formatter.format(1, 2, 3, 4))
# prints 4 strings with spaces in between
print (formatter.format("one", "two", "three", "four"))
# prints 4 booleans with spaces in between
print (formatter.format(True, False, False, True))
# prints formatter string 4 times with spaces in between
print (formatter.format(formatter, formatter, formatter, formatter))
# prints 4 strings with spaces in between
print (formatter.format(
        "Try your",
        "Own text here",
        "Maybe a poem",
        "Or a song about fear"
        ))
