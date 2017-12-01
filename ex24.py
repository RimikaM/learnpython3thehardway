# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 00:35:08 2017

@author: rimikamajumdar
"""

# Exercise 24: More Practice

# printing stuff
print("Let's practice everything.")
print("You\'d need to know \'bout escapes with \\ that do.")
print("\n newlines and \t tabs.")

# string variable
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

# printing stuff
print("--------------")
print(poem)
print("--------------")

# variable five = 5 and print it
five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    # return three values
    return jelly_beans, jars, crates

start_point = 10000
# assign three variables to the output of secret_formula()
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point /= 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates".format(*formula))

'''
Output is the following:
Let's practice everything.
You'd need to know 'bout escapes with \ that do.

 newlines and    tabs.
--------------

        The lovely world
with logic so firmly planted
cannot discern 
 the needs of love
nor comprehend passion from intuition
and requires an explanation

        where there is none.

--------------
This should be five: 5
With a starting point of: 10000
We'd have 5000000 beans, 5000.0 jars, and 50.0 crates.
We can also do that this way:
We'd have 500000.0 beans, 500.0 jars, and 5.0 crates
'''