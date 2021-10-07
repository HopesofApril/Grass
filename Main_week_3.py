# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 22:24:24 2021

@author: 수미니
"""

n = int(input())
s = 0

for i in range(1,1+n):
    if i%2 == 0:
        s = s + i
        
print(s)