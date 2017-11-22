# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 13:56:41 2017

@author: rimikamajumdar
"""

# Exercise 14: Prompting and Passing

from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}m I'm the {script} script.")
print(f"I'd like to ask you a few questions")
print(f"Do you like me {user_name}?")
# prints out > for user_name to enter their response
likes = input(prompt)

print(f"Where do you live {user_name}?")
location = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {location}. Not sure where that is.
And you have a {computer} computer. Nice.
""")

