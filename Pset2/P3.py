#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 15:02:57 2020

@author: Andrew
"""


# End of year balance
balance = 0
annualInterestRate = 0




def lowest(balance, annualInterestRate):
    def check(balance, annualInterestRate, monthlyPayment):
        for i in range(12):
            balance = (balance - monthlyPayment) + (balance - monthlyPayment)*(annualInterestRate/12)
        return balance
    
    lowerBound = balance/12
    upperBound = (balance * (1 + annualInterestRate/12)**12)/12.0
    midBound = (lowerBound+upperBound)/2
    new_rate = check(balance, annualInterestRate, midBound)
    while new_rate >= 0.01 or new_rate <= -0.01:
        if new_rate >= 0.01:
            lowerBound = midBound
            midBound = (lowerBound+upperBound)/2
            new_rate = check(balance, annualInterestRate, midBound)
        if new_rate <= -0.01:
            upperBound = midBound
            midBound = (lowerBound+upperBound)/2
            new_rate = check(balance, annualInterestRate, midBound)
        
    print('Lowest Payment: ' + str(round(midBound,2)))

lowest(balance, annualInterestRate)


