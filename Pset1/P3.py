#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 17:04:09 2020

@author: Andrew
"""

s = 'azcbobobegghakl'

iteration = len(s) - 1
ans = 0
for x in range(iteration):
    if s[x:x+3] == 'bob':
        ans += 1
print("Number of times bob occurs is: " + str(ans))

for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print('Current Letter :', letter)