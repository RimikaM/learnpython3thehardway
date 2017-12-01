# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 00:14:42 2017

@author: rimikamajumdar
"""

# Exercise 28: Boolean Practice
# remember: any 'and' expression that has a False is immediately False!

print("1", True and True) #True
print("2", False and True) #False
print("3", 1 == 1 and 2 == 1) #True and False -> False
print("4", "test" == "test") #True 
print("5", 1 == 1 or 2 != 1) #True or False -> True
print("6", True and 1 == 1) #True
print("7", False and 0 != 0) #False and False -> False
print("8", True or 1 == 1) #True
print("9", "test" == "testing") #False
print("10", 1 != 0 and 2 == 1) #True and False -> False
print("11", "test" != "testing") #True
print("12", "test" == 1) #False
print("13", not (True and False)) #not False -> True
print("14", not (1 == 1 and 0 != 1)) #not True -> False
print("15", not (10 == 1 or 1000 == 1000)) #not True -> False
print("16", not (1 != 10 or 3 == 4)) #not True -> False
print("17", not ("testing" == "testing" and "Rimika" == "awesome")) #not False -> True
print("18", 1==1 and (not ("testing" == 1 or 1 == 0))) #True and (not False) -> True
print("19", "chunky" == "bacon" and (not (3 == 4 or 3 == 3))) #False and (not True) -> False
print("20", 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))) #True and (not True) -> False