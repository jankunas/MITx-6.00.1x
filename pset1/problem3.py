# -*- coding: utf-8 -*-
"""
@author: Saras

Problem Set 1 for MITx: 6.00.1x Introduction to Computer Science and Programming Using Python
"""

'''
Problem 3
15.0/15.0 points (graded)
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
'''
from itertools import count

maxsubstr = s[0:0] 
for start in range(len(s)): 
    for end in count(start + len(maxsubstr) + 1): 
        substr = s[start:end] 
        if len(substr) != (end - start): 
            break
        if sorted(substr) == list(substr):
            maxsubstr = substr
            
print ("Longest substring in alphabetical order is: " + str(maxsubstr))