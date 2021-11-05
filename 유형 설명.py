# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 21:11:01 2021

@author: 수미니
"""

test = str(input('테스트 결과는?(영어 대문자로 적어주세요) '))

#공통문장
#꾸준히/벼락치기 #선생/학생 #외부/내부 #그룹/개인
#(한 번에 몰아서, 꾸준히) 공부하고 (선생님/학생) 스타일인 당신은 (조용한 분위기/약간의 소음이 있는 카페등)에서 (다같이/혼자) 학습하는 것을 선호하는 편입니다


# 8가지 유형
#꾸준히 공부
C = '체계적으로 계획을 세워 꾸준히 공부하고 깊이 있게 공부하는 것을 선호하는 스타일입니다.'
#벼락치기
H = '시간이 촉박해 아슬아슬 위태롭지만 그 스릴을 즐기는 당신은 짧은 시간 확실하게 집중해서 고효율 학습을 선호하는 스타일입니다.'
#선생님 형
T = '본인이 이해한 내용을 타인 혹은 스스로에게 설명하는 것에 즐거움을 느낌과 동시에 질문을 설명하기 위해 추가적으로 공부하는 것을 좋아합니다.'
#학생 형
S = '타인의 설명을 듣고 오랜 시간 이해하고 질문이 생길 시 물어보는 것을 좋아하고 주변 환경이 공부 분위기로 형성되면 더 집중을 잘할 수 있습니다.'
#외부형
O = '약간 소음이 있고 긴장감 느껴지는 카페 같은 외부에서 학습하는 것을 좋아합니다.'
#내부형
I = '독서실 혹은 집과 같은 조용한 내부에서 집중하며 공부하는 것을 좋아합니다.'
#그룹형
G = '친구들과 다 같이 모여서 스터디 모임을 만들고 자극받아 공부하는 것을 좋아합니다.'
#개인형
A = '공부는 나 자신과의 싸움이라 생각하며 혼자 공부하는 것이 집중이 잘됩니다.'

# 공부 방법 추천
#꾸준히,벼락치기
ch = '계획을 세워서 공부하는 것을 추천하며, 계획한 일이 제대로 되지 않았을 경우에는 그날 일과를 검토해보고 계획을 수정해 실천하는 것을 추천합니다.'
#선생님/학생형
t = '타인과 멘토&멘티를 맺어 공부하는 것을 추천하며, 멘티에게 설명하고 그의 질문에 답변하는 방식으로 공부하는 것을 추천합니다.'
s = '타인과 멘토&멘티를 맺어 공부하는 것을 추천하며, 멘토에게 설명을 듣고 질문하는 방식으로 공부하는 것을 추천합니다'
#그룹형/개인형
g = '스터디 모임을 만들어 공부하는 것을 추천하지만, 집중이 흐트러질 수 있다는 단점이 있기 때문에 그룹 내의 규칙을 정해서 공부하는 것을 추천합니다. (예시: 1시간 동안 집중해서 공부, 만약 떠들면 벌칙 수행하기)'
a = '혼자 공부하기 때문에 집중하는 게 중요한데, 백지에 필기하며 공부하는 것을 추천합니다.'

while True:
    if test == 'CTOG':
        print(C,T,O,G)
        print(ch,t,g)
        break
    elif test == 'CTOA':
        print(C,T,O,A)
        print(ch,t,a)
        break
    elif test == 'CTIG':
        print(C,T,I,G)
        print(ch,t,g)
        break
    elif test == 'CTIA':
        print(C,T,I,A)
        print(ch,t,a)
        break
    elif test == 'CSOG':
        print(C,S,O,G)
        print(ch,s,g)
        break
    elif test == 'CSOA':
        print(C,S,O,A)
        print(ch,s,a)
        break
    elif test == 'CSIG':
        print(C,S,I,G)
        print(ch,s,g)
        break
    elif test == 'CSIA':
        print(C,S,I,A)
        print(ch,s,a)
        break
    elif test == 'HTOG':
        print(H,T,O,G)
        print(ch,t,g)
        break
    elif test == 'HTOA':
        print(H,T,O,A)
        print(ch,t,a)
        break
    elif test == 'HTIG':
        print(H,T,I,G)
        print(ch,t,g)
        break
    elif test == 'HTIA':
        print(H,T,I,A)
        print(ch,t,a)
        break
    elif test == 'HSOG':
        print(H,S,O,G)
        print(ch,s,g)
        break
    elif test == 'HSOA':
        print(H,S,O,A)
        print(ch,s,a)
        break
    elif test == 'HSIG':
        print(H,S,I,G)
        print(ch,s,g)
        break
    elif test == 'HSIA':
        print(H,S,I,A)
        print(ch,s,a)
        break
    else:
        print('잘못입력하셨습니다. 다시 입력해주세요')
        test = str(input('테스트 결과는?(영어 대문자로 적어주세요) '))