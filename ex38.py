# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 21:07:07 2017

@author: rimikamajumdar
"""

# Exercise 38: Doing Things to Lists

'''
When to use lists:
    - if you need to maintain listed order
    - need to access contents randomly by #
    - need to go through the contents linearly
'''


ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

# splits ten_things string by spaces into a list
stuff = ten_things.split(" ")

# new list
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while (len(stuff) != 10):
    # remove first item from more_stuff and assign string to next_one
    next_one = more_stuff.pop()
    
    print(f"Adding: {next_one}")
    # add next_one to the end of stuff
    stuff.append(next_one)
    
    # length with now increment by 1
    print(f"There are {len(stuff)} items now.")
    
print(f"There we go: {stuff}")

print("Let's do some things with stuff.")

# 2nd item in stuff
print(stuff[1])

# last item in stuff
print(stuff[-1])

# first item in stuff
print(stuff.pop())

# convert list to a string separated by spaces and print it
print(' '.join(stuff))

# convert list to string separated by # and print the 4th and 5th word 
print('#'.join(stuff[3:5]))
      
'''
Output is the following:
Wait there are not 10 things in that list. Let's fix that.
Adding: Boy
There are 7 items now.
Adding: Girl
There are 8 items now.
Adding: Banana
There are 9 items now.
Adding: Corn
There are 10 items now.
There we go: ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana', 'Corn']
Let's do some things with stuff.
Oranges
Corn
Corn
Apples Oranges Crows Telephone Light Sugar Boy Girl Banana
Telephone#Light
'''