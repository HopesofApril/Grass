# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 21:52:40 2021

@author: 수미니
"""

num = int(input("0~1000 사이의 정수를 입력하세요: "))
hap = 0
s = 0

while True:
    if num > 1000:
        num = int(input("1000을 초과했어요. 0~1000 사이의 정수를 입력하세요: "))
    else:
        hap = hap + s
        s = s + 1
        if hap >= num:
            print(s-1)
            break