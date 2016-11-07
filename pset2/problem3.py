# -*- coding: utf-8 -*-
"""
@author: Saras

Problem Set 2 for MITx: 6.00.1x Introduction to Computer Science and Programming Using Python
"""

'''
Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on 
bisection search) to find the smallest monthly payment to the cent (no more multiples of $10) such that we 
can pay off the debt within a year. Try it out with large inputs, and notice how fast it is (try the same 
large inputs in your solution to Problem 2 to compare!). Produce the same return value as you did in Problem 2.
'''

balance = 320000
annualInterestRate = 0.2
epsilon = 0.01

monthlyInterestRate = annualInterestRate/12
originalBalance = balance
monthlyPaymentLowerBound = balance/12
monthlyPaymentUpperBound =  (balance * (1 + monthlyInterestRate)**12) / 12.0

while abs(balance) > epsilon:
    balance = originalBalance
    payment = (monthlyPaymentUpperBound - monthlyPaymentLowerBound) / 2 + monthlyPaymentLowerBound
    for month in range(12):
        balance -= payment
        balance *= 1 + monthlyInterestRate
    if balance > 0:
        monthlyPaymentLowerBound = payment
    else:
        monthlyPaymentUpperBound = payment

print ("Lowest Payment: ", round(payment, 2))