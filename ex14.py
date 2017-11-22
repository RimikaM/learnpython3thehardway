# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 13:56:41 2017

@author: rimikamajumdar
"""

# Exercise 14: Prompting and Passing

from sys import argv

script, user_name, subject = argv
prompt = '> '

print(f"Hi {user_name} I'm the {script} script.")
print(f"I'd like to ask you a few questions")
print(f"Do you like me {user_name}?")
# prints out > for user_name to enter their response
likes = input(prompt)

print(f"I see you want to talk about {subject}")
print(f"So {user_name}, how do you feel about {subject}?")
opinion = input(prompt)

print(f"Where do you live {user_name}?")
location = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You have a {opinion} opinion about {subject}.
You live in {location}. Not sure where that is.
And you have a {computer} computer. Nice.
""")

'''
printed the following:
Hi Rimika I'm the ex14.py script.
I'd like to ask you a few questions
Do you like me Rimika?
> sure
I see you want to talk about dancing
So Rimika, how do you feel about dancing?
> happy
Where do you live Rimika?
> a place
What kind of computer do you have?
> dell
Alright, so you said sure about liking me.
You have a happy opinion about dancing.
You live in a place. Not sure where that is.
And you have a dell computer. Nice.
'''