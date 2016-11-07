# -*- coding: utf-8 -*-
"""
@author: Saras

Problem Set 1 for MITx: 6.00.1x Introduction to Computer Science and Programming Using Python
"""

'''
Problem 1
10.0/10.0 points (graded)
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
'''
counter = 0
for n in s:
    if 'a' == n:
        counter += 1
    if 'e' == n:
        counter += 1
    if 'i' == n:
        counter += 1
    if 'o' == n:
        counter += 1
    if 'u' == n:
        counter += 1
print('Number of vowels: ' + str(counter))

