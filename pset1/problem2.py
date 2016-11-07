# -*- coding: utf-8 -*-
"""
@author: Saras

Problem Set 1 for MITx: 6.00.1x Introduction to Computer Science and Programming Using Python
"""

'''
Problem 2
10.0/10.0 points (graded)
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
'''
counter = 0
c = len(s)
final = 0

while counter < c-2:
    letter = s[counter]
    if (s[counter] == 'b'and s[counter+1] == 'o'and s[counter+2] == 'b'):
        final += 1
    counter += 1
                
print('Number of times bob occurs is: ' + str(final))