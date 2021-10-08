# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 19:42:33 2021

@author: 수미니
"""


alpha = str(input ("알파벳 소문자를 입력해주세요: "))

while True:
    if alpha == "q":
        print(alpha)
        break
    else:
        print(alpha)
        alpha = input ("알파벳 소문자를 입력해주세요: ")
    