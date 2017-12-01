# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 22:02:58 2017

@author: rimikamajumdar
"""
# use functions from ex25.py
import ex25
sentence = "All good things come to those who wait."
words = ex25.break_words(sentence)
# words -> ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
print(words)

sorted_words = ex25.sort_words(words)
# sorted_words -> ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
print(sorted_words)

# All
ex25.print_first_word(words)

# wait.
ex25.print_last_word(words)

# words -> ['good', 'things', 'come', 'to', 'those', 'who']
print(words)

# All
ex25.print_first_word(sorted_words)

# who
ex25.print_last_word(sorted_words)

# sorted_words -> ['come', 'good', 'things', 'those', 'to', 'wait.']
print(sorted_words)

sorted_words = ex25.sort_sentence(sentence)
# sorted_words -> ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
print(sorted_words)

'''
All
wait.
'''
ex25.print_first_and_last(sentence)

'''
All
who
'''
ex25.print_first_and_last_sorted(sentence)