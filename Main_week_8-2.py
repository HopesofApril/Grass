# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 12:25:32 2021

@author: 수미니
"""

#16진수 구구단 출력하기
#A~F 중 하나 입력시 1~F까지 곱한 16진수 구구단

#A~F에 해당하는 값 입력받기, 16 인수 추가 > 16진수 int 형
num = int(input('A~F 중 하나를 입력하세요: '), 16)

#가장 마지막인 F는 10진수로 변경시 15가 되므로 1을 더해준 16까지 돌아야 함
for i in range (1,16):
    #16 진수 포맷 코드 %X를 사용해 16진수로 출력
    #('%X'%n)은 n에 저장된 값을 16진수 형태로 출력
    #num은 처음 입력받은 값, i는 1에서 16까지 1씩 더해져서 나오는 값, num*i는 둘을 곱한 값
    #sep=''은 공백없이 출력
    
    print('%X'%num, '*%X'%i, '=%X'%(num*i), sep='')
    #print('%X*%X=%X' %(num,i,(num*i)))
    #print('%X * %X = %X' %(num,i,(num*i)))