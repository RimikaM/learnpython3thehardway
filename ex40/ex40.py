# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 21:59:41 2017

@author: rimikamajumdar
"""

# Exercise 40: Modules, Classes, and Objects

# Modules Are Like Dictionaries
mystuff = {'apple': "I AM APPLES!"}
# get 'apple' from dict
# prints -> I AM APPLES!
print(mystuff['apple'])

# import module mystuff.py
import mystuff
# get apple() from module
# prints -> I AM APPLES!
mystuff.apple()
# get variable tangerine from module
# prints -> Living reflection of a dream
print(mystuff.tangerine)



class Learning(object):
    
    def __init__(self):
        self.tangerine = "And now a thousand years between"
        
    def apple(self):
        print("I AM CLASSY APPLES!")
        
thing = Learning()
'''
I AM CLASSY APPLES!
And now a thousand years between
'''
thing.apple()
print(thing.tangerine)



class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
            
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])
    
bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

'''
Happy birthday to you
I don't want to get sued
So I'll stop right there
'''    
happy_bday.sing_me_a_song()

'''
They rally around tha family
With pockets full of shells
'''
bulls_on_parade.sing_me_a_song()