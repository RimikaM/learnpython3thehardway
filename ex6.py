#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 11:27:03 2017

@author: rimikamajumdar
"""

# Exercise 6: Strings and text

types_of_people = 10
# types_of_people integer put inside a format string
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
# binary string and do_not string put inside a forma
y = f"Those who know {binary} and those who {do_not}."

# print x and y strings on separate lines
print(x)
print(y)

# print x format string inside another format string
print(f"I said: {x}")
# print y format string inside another format string
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# print hilarious boolean inside joke_evaluation string
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# print concatenation of w and e
print(w+e)