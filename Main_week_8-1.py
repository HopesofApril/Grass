# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 21:02:58 2021

@author: 수미니
"""

#주사위 2개 던지기
#1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때 나올 수 있는 경우의 수

#주사위 면 입력받기
n = int(input('첫번째 주사위의 면은 몇개인가요? (10이하의 자연수) '))
m = int(input('두번째 주사위의 면은 몇개인가요? (10이하의 자연수) '))

#입력받은 면의 수만큼 반복(반복하면서 1씩 더해짐, 그대로 출)
for dice_1 in range (1,n+1):
    for dice_2 in range (1, m+1):
        print(dice_1, dice_2)