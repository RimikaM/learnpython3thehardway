# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 22:49:03 2017

@author: rimikamajumdar
"""

# Exercise 33: While Loops
# while loops run until the expression is false

'''
1. Convert this while-loop to a function that you can call, and replace 6 in the
    test (i < 6) with a variable
2. Use this function to rewrite the script to try different numbers
3. Add another variable to the function arguments that you can pass in that
    lets you change the +1 in line 27 so you can change the increment value.
4. Rewrite the script again to use this function to see what effect it has
5. Write it to use for-loops and range.

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)
    
    i += 1
    print("Numbers now:", numbers)
    print(f"At the bottom i is {i}")
'''

def append_num(num_iterations, increment):
    numbers = []
    for num in range(0, num_iterations):
        print(f"At the top i is {num}")
        numbers.append(num)
        num += increment
        print("Numbers now:", numbers)
        print(f"At the bottom i is {num}")
    return numbers
    
print("The numbers: ")

numbers = append_num(6, 1)

for num in numbers:
    print(num)
    

'''
Output is the following:
At the top i is 0
Numbers now: [0]
At the bottom i is 1
At the top i is 1
Numbers now: [0, 1]
At the bottom i is 2
At the top i is 2
Numbers now: [0, 1, 2]
At the bottom i is 3
At the top i is 3
Numbers now: [0, 1, 2, 3]
At the bottom i is 4
At the top i is 4
Numbers now: [0, 1, 2, 3, 4]
At the bottom i is 5
At the top i is 5
Numbers now: [0, 1, 2, 3, 4, 5]
At the bottom i is 6
The numbers: 
0
1
2
3
4
5
'''