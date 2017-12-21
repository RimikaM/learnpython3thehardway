# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 23:04:30 2017

@author: rimikamajumdar
"""

from nose.tools import *
import ex46

def setup():
    print("SETUP!")
    
def teardown():
    print("TEAR DOWN!")
    
def test_basic():
    print("I RAN!")