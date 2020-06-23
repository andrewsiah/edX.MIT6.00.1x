#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 17:04:09 2020

@author: Andrew
"""


count = 0
for char in s:
    if char in 'aeiou':
        count += 1

print("Number of vowels: " + str(count))