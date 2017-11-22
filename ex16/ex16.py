# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 14:34:18 2017

@author: rimikamajumdar
"""

# Exercise 16: Reading and Writing Files
# simple text editor

'''
Important commands to remember:
    * close() - closes the files
    * read() = reads the contents of the file.
    * readline() - reads just one line of a text file
    * truncate() - empties the file.
    * write('stuff') - writes 'stuff' to the file
    * seek(0) - moves the read/write location tothe beginning of the file
        (like a tape and DVD drive)
'''

from sys import argv 

script, filename = argv

print(f"We're going to erase {filename}")
print(f"If you don't want that, hit CTRL-C (^C).")
print(f"If you do want to do that, hit RETURN.")

input("? ")

print("Opening the file...")
# open file in write mode
# open(filename) defaults to read mode
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
# it is repetitive to truncate the file when it is in write mode
# because it will be overwritten anyway
target.truncate()

print("Now I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
new_line = "\n"
target.write(line1 + new_line + line2 + new_line + line3 + new_line)

print("And finally, we close it.")
target.close()

'''
Output is the following:
We're going to erase ex16_sample.txt
If you don't want that, hit CTRL-C (^C).
If you do want to do that, hit RETURN.
? 
Opening the file...
Truncating the file. Goodbye!
Now I'm going to ask you for three lines.
line 1: hello
line 2: I am cool
line 3: k bye
I'm going to write these to the file.
And finally, we close it.
'''
