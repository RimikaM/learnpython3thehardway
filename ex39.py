# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 21:57:43 2017

@author: rimikamajumdar
"""

# Exercise 39: Dictionaries, Oh Lovely Dictionaries


'''
# Remember, you can only use numbers to get items out of a list
>>> things = ['a', 'b', 'c', 'd']
>>> print(things[1])
b
>>> things[1] = 'z'
>>> print(things[1])
z
>>> things
['a', 'z', c', 'd']
'''

'''
# a dict lets you use any data type
>>> stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}
>>> print(stuff['name'])
Zed
>>> print(stuff['age'])
39
>>> print(stuff['height'])
74
>>> stuff['city'] = 'SF'
>>> print(stuff['city'])
SF

>>> stuff[1] = "Wow"
>>> stuff[2] = "Neato"
>>> print(stuff[1])
Wow
>>> print(stuff[2])
Neato
'''

'''
# deleting things from a dict
>>> del stuff['city']
>>> del stuff[1]
>>> del stuff[2]
>>> stuff
{'name': 'Zed', 'age': 39, 'height': 74}
'''





'''
A DICTIONARY EXAMPLE
'''

# a dict is like a database for storing and organizing data
# a dict doesn't have order
# a dict matches "keys" to "values"
# use a dict when you have to take one value and look up another value
# use a list for any sequence that needs to be in order
# collections.OrderedDict data structure is a dict with order


# create a mapping of state to abbreviation
states = {
        'Oregon': 'OR',
        'Florida': 'FL',
        'California': 'CA',
        'New York': 'NY',
        'Michigan': 'MI'
        }

# create a basic set of states and some cities in them
cities = {
        'CA': 'San Francisco',
        'MI': 'Detroit',
        'FL': 'Jacksonville'
        }

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print(f"NY State has: {cities['NY']}")
print(f"OR State has: {cities['OR']}")

# print some states
print('-' * 10)
print(f"Michigan's abbreviation is: {states['Michigan']}")
print(f"Florida's abbreviation is: {states['Florida']}")

# do it by using the state then cities dict
print('-' * 10)
print(f"Michigan has: {cities[states['Michigan']]}")
print(f"Florida has: {cities[states['Florida']]}")

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    
# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")
    
# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")
    
print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")
    
# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")

'''
Output is the following:
    
----------
NY State has: New York
OR State has: Portland
----------
Michigan's abbreviation is: MI
Florida's abbreviation is: FL
----------
Michigan has: Detroit
Florida has: Jacksonville
----------
Oregon is abbreviated OR
Florida is abbreviated FL
California is abbreviated CA
New York is abbreviated NY
Michigan is abbreviated MI
----------
CA has the city San Francisco
MI has the city Detroit
FL has the city Jacksonville
NY has the city New York
OR has the city Portland
----------
Oregon state is abbreviated OR
and has city Portland
Florida state is abbreviated FL
and has city Jacksonville
California state is abbreviated CA
and has city San Francisco
New York state is abbreviated NY
and has city New York
Michigan state is abbreviated MI
and has city Detroit
----------
Sorry, no Texas.
The city for the state 'TX' is: Does Not Exist
'''