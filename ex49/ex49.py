# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 22:54:31 2017

@author: rimikamajumdar
"""

import parser

x = parse_sentence([('verb', 'run'), ('direction', 'north')])

print(x.subject)
# player

print(x.verb)
# run

print(x.object)
# north

x = parse_sentence([('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'),
                    ('noun', 'honey')])

print(x.subject)
# bear

print(x.verb)
# eat

print(x.object)
# honey