# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 17:21:21 2017

@author: rimikamajumdar
"""

# Exercise 19: Functions and Variables

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man, that's enough for a party!")
    print("Get a blanket.\n")
    
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from out script:")
cheese = 10
crackers = 50
cheese_and_crackers(cheese, crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(cheese + 100, crackers + 1000)

'''
Output is the following:
We can just give the function numbers directly:
You have 20 cheeses!
You have 30 boxes of crackers!
Man, that's enough for a party!
Get a blanket.

OR, we can use variables from out script:
You have 10 cheeses!
You have 50 boxes of crackers!
Man, that's enough for a party!
Get a blanket.

We can even do math inside too:
You have 30 cheeses!
You have 11 boxes of crackers!
Man, that's enough for a party!
Get a blanket.

And we can combine the two, variables and math:
You have 110 cheeses!
You have 1050 boxes of crackers!
Man, that's enough for a party!
Get a blanket.
'''