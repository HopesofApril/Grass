# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 01:29:52 2021

@author: 수미니
"""

#사용할 라이브러리 import
import pandas as pd
import numpy as np

#데이터셋 불러오기
train_set = pd.read_csv('train.csv')

#데이터셋이 어떻게 생겼는지 확인해보기
train_set.head(3)

test_set = pd.read_csv('test.csv')
test_set.head(3)

#데이터에 null 값이 있는지 확인하기
train_set.isnull().sum()
test_set.isnull().sum()

#null값을 어떤 식으로 처리할지 고민해보기
train_set.fillna("S")

#타겟 데이터 변수 할당

#타겟 데이터 따로 저장
target_sur = train_set['Survived']

#타겟데이터와 불필요데이터 삭제
train_set.drop(labels=['Name'],axis=1,inplace=True)
train_set.drop(labels=['Cabin'],axis=1,inplace=True)
train_set.drop(labels=['Fare'],axis=1,inplace=True)
train_set.drop(labels=['Ticket'],axis=1,inplace=True)
train_set.drop(labels=['Embarked'],axis=1,inplace=True)
train_set.head()

#성별 데이터를 숫자로 변환
train_set['Sex'] = train_set['Sex'].map({"female":"1","male":"2"})

#입력 데이터가 제대로 준비되었는지 확인
train_set

x_train = train_set.drop(labels=['Survived'],axis=1)

x_train

#타겟데이터와 불필요데이터 삭제
test_set.drop(labels=['Name'],axis=1,inplace=True)
test_set.drop(labels=['Cabin'],axis=1,inplace=True)
test_set.drop(labels=['Fare'],axis=1,inplace=True)
test_set.drop(labels=['Ticket'],axis=1,inplace=True)
test_set.drop(labels=['Embarked'],axis=1,inplace=True)
test_set.head()

#성별 데이터를 숫자로 변환
test_set['Sex'] = test_set['Sex'].map({"female":"1","male":"2"})

#입력 데이터가 제대로 준비되었는지 확인
test_set

#로지스틱 회귀 모델 생성 후 모델 훈련
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(x_train,target_sur)

#예측 결과 출력
lr.predict(test_set)

#가상의 승객이 탑승하였을 때 조건을 가정하여 생존확률을 예측
tt = lr.predict([[100,1,1,20,1,2]])
if tt == 1:
    print("생존")
else:
    print("사망")