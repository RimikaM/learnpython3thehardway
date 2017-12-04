# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 20:14:00 2017

@author: rimikamajumdar
"""

# Exercise 35: Branches and Functions

from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")
    
    choice = input("> ")
    if (not int(choice)):
        dead("Man, learn how to type a number.")
    how_much = int(choice)
    
    if (how_much < 50):
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")
        
        
def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False
    
    # makes an infinite loop
    while True:
        choice = input("> ")
        
        if ("take honey" in choice):
            dead("The bear looks at you then slaps your face off.")
        elif ("taunt bear" in choice and not bear_moved):
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif ("taunt bear" in choice and bear_moved):
            dead("The bear gets pissed off and chews your leg off.")
        elif ("open door" in choice and bear_moved):
            gold_room()
        else:
            print("I got no idea what that means.")
            

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever starres at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    
    choice = input("> ")
    
    if ("flee" in choice):
        start()
    elif ("head" in choice):
        dead("Well that was tasty!")
    else:
        cthulhu_room()
            
            
def dead(why):
    print(why, "Good job!")
    exit(0)
    
    
def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    
    choice = input("> ")
    
    if ("left" in choice):
        bear_room()
    elif ("right" in choice):
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")
        
        
        
start()

'''
Output is the following:
You are in a dark room.
There is a door to your right and left.
Which one do you take?
> left
There is a bear here.
The bear has a bunch of honey.
The fat bear is in front of another door.
How are you going to move the bear?
> taunt bear
The bear has moved from the door.
You can go through it now.
> open door
This room is full of gold. How much do you take?
> 1000
You greedy bastard! Good job!
'''