# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 12:54:09 2017

@author: rimikamajumdar
"""

# Exercise 31: Making Decisions
# ask the user questions and make decisions based on their answers 

print(""" 
You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if (door == "1"):
    print("There's a giant bear here eating a cheesecake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    
    bear = input("> ")
    
    if (bear == "1"):
        print("The bear eats your face off. Good job!")
    elif (bear == "2"):
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("\n\nFour unfortune/fortune cookies appear in front of you that will decide your fate.")
        print("Three of them are tragic, and one contains good news.")
        print("Which one do you choose?")
        print("1, 2, 3, or 4?")
        
        cookie = input("> ")
        if (cookie == "1"):
            print("Congrats! Your friends are coming to rescue you from the bear :D")
        elif (cookie == "2"):
            print("Sorry, the bear mistook you for a cake and ate you!")
        elif (cookie == "3"):
            print("Yay!!! The bear ran away because you didn't seem appetizing enough!")
            print("......Hmmmmm....spoke too soon!")
            print("Because you were so shocked, you tripped and fell of a cliff!!!")
        elif (cookie == "4"):
            print("Your friends came to rescue you from the bear....")
            print("However, your friend Bella gave you a drink that had poison in it...")
            print("And then you slowly died.................")
        else:
            print("Your eyes rot into a pool of muck.....")
        
elif (door == "2"):
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    
    insanity = input("> ")
    
    if (insanity == "1" or insanity == "2"):
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
        
else:
    print("You stumble around and fall on a knife and die. Good job!")
    