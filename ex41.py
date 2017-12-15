# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 22:52:38 2017

@author: rimikamajumdar
"""

# Exercise 41: Learning to Speak Object Oriented
# Object Oriented Programming Test!!!

'''
run script with:
    $ python ex41.py english
'''

import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
# empty list
WORDS = []

# dictionary
PHRASES = {
        "class %%%(%%%):": 
            "Make a class named %%% that is-a %%%.",
        "class %%%(object):\n\tdef __init__(self, ***)":
            "class %%% has-a __init__ that take self and *** params.",
        "class %%%(object):\n\tdef ***(self, @@@)":
            "class %%% has-a function *** that takes self and @@@ params.",
        "*** = %%%()":
            "Set *** to an instance of class %%%.",
        "***.***(@@@)":
            "From *** get the *** function, call it with params self, @@@.",
        "***.*** = '***'":
            "From *** get the *** attribute and set it to '***'."
        }
    
# do they want to drill phrases first
# run the script with the 'english' option!
if len(sys.argv) == 2 and sys.argv[1] == 'english':
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False
    
# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))
    
    
def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("%%%"))
    results = []
    param_names = []
    
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))
        
    for sentence in snippet, phrase:
        # python's way of copying a list
        result = sentence[:]
        
        # fake class names
        for word in class_names:
            # replacing words with something else
            result = result.replace("%%%", word, 1)
            
        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)
            
        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)
            
        results.append(result)
        
    return results

# keep going until they hit CTRL-D
try:
    while True:
        # print task for the user to do, and user and enters it after >
        # then correct answer prints out
        
        '''
        Example:
        From *** get the *** attribute and set it to '***'.

        > ***.*** = '***'
        ANSWER:  ***.*** = '***' 
        
        
        From *** get the *** function, call it with params self, apple, color, adjustment.

        > ***.***(apple, color, adjustment)
        ANSWER:  ***.***(apple, color, adjustment)
        
        
        class Cushion has-a function bone that takes self and ant, advice params.

        > class Cushion(object): def bone(self, ant, advice)
        ANSWER:  class Cushion(object):
                def bone(self, ant, advice)
        '''
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)
        
        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question
                
            print(question)
            
            input("> ")
            print(f"ANSWER:  {answer}\n\n")
            
# do the try statement until the end of file is reached and print Bye!
except EOFError:
    print("\nBye")