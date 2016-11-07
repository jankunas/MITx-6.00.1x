# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 11:55:14 2016

Problem Set 2 for MITx: 6.00.1x Introduction to Computer Science and Programming Using Python
"""

'''
Problem 2 - Paying Debt Off in a Year
15.0 points possible (graded)
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:

Lowest Payment: 180 
'''
balance = 3926
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12.0
minimumFixedMonthlyPayment = 10
originalBalance = balance
while True:
    balance = originalBalance
    monthlyUnpaidBalance = 0
    updatedBalance = 0
    for month in range(12):
        monthlyUnpaidBalance = balance - minimumFixedMonthlyPayment
        updatedBalance = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)    
        balance = updatedBalance
    if monthlyUnpaidBalance <= 0:
        break
    minimumFixedMonthlyPayment = minimumFixedMonthlyPayment + 10
print('Lowest payment: %.2f' % minimumFixedMonthlyPayment)

    
    
