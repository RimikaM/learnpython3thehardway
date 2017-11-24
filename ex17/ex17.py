# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 15:00:19 2017

@author: rimikamajumdar
"""

# Exercise 17: More files
# python script to copy one file to another

from sys import exit
from sys import argv
from os.path import exists    
    
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
#in_file = open(from_file)
#indata = in_file.read()
# file should be closed by Python once the line runs
if (exists(from_file) == False):
    exit(f"The {from_file} file does not exist")
indata = open(from_file).read()

print(f"The input file is {len(indata)} bytes long")

# exists returns true if file exists, false if not
# below line is not necessary because if the out_file doesn't exist,
# Python creates it
#print(f"Does the output file exist? {exists(to_file)}")
#print("Ready, hit RETURN to continue, CTRL-C to abort")
#input()

#out_file = open(to_file, 'w')
#out_file.write(indata)
out_file = open(to_file, 'w').write(indata)

print("Alright, all done.")

#out_file.close()
#in_file.close()

'''
Output is the following:
Copying from test.txt to new_file.txt
The input file is 20 bytes long
Alright, all done.
'''