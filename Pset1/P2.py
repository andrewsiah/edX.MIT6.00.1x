#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 17:04:09 2020

@author: Andrew
"""


count = 0
for i in range(len(s)-2):
    temp = s[i:i+3] 
    if temp == 'bob':
        count += 1

print("Number of times bob occurs is: " + str(count))