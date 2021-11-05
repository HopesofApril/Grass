# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 12:20:04 2021

@author: 수미니
"""

#라이브러리 호출
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#리뷰 데이터 수집 및 수집된 데이터 저장 프레임 제작
data = pd.DataFrame(data=[], columns=["아이디","리뷰","별점- 상품","별점- 배송","날짜"])

#티몬 원하는 상품 페이지 이동
driver = webdriver.Chrome("chromedriver.exe")
url = 'http://mobile.tmon.co.kr/deals/2608649266?deal_srl=2608649266&keyword=%ED%98%B8%EB%B9%B5&tl_area=MWSALL&tl_ord=6&searchClick=DL%7CND%7CBM&thr=ms'
driver.get(url)
sleep(1)

#그 중에서도 리뷰 데이터 수집 목적이므로 리뷰 데이터 버튼 클릭
driver.find_element_by_xpath('//*[@id="_dealReviewWrap"]/div[1]/div[2]/button').send_keys(Keys.ENTER)
sleep(1)

#스크롤 다운 함수
def scroll_down(driver, k):
    last_height = 0
    try_count = 0
    scroll_count = 0
    
    while True:
        now_height = driver.execute_script('return document.body.scrollHeight;')
        if last_height == now_height:
            if k > 10:
                break
            
        else:
            try_count = 0
            scroll_count += 1
            if scroll_count > k:
                break
            
        last_height = now_height
        driver.execute_script('window.scroll(0, document.body.scrollHeight);')
        sleep(0.5)
        try_count += 1

#리뷰 수집 함수
def crawl(driver, data, k):
    
    #아이디 수집
    user_ID = driver.find_elements_by_css_selector('#_reviewList > li> div > ul > li:nth-child(1)')
    #리뷰 수집
    text_review = driver.find_elements_by_css_selector('#_reviewList > li> div > div.review_block_text > div')
    #별점 수집_상품
    star_block_score = driver.find_elements_by_xpath('//*[@id="_reviewList"]/li/div/div[1]/div[1]/span[2]/span/span')
    #별점 수집_배송
    star_progress_score = driver.find_elements_by_xpath('//*[@id="_reviewList"]/li/div/div[1]/div[2]/span[2]/span/span')
    #날짜 수집
    date = driver.find_elements_by_css_selector('#_reviewList > li > div > ul > li:nth-child(2)')
    
    #k개의 리뷰 수집
    for i in range (k):
        #global tmp
        tmp_ID= []
        tmp_review= []
        tmp_star_block= []
        tmp_star_progress= []
        tmp_date= []
        tmp_ID.append(user_ID[i].text)
        tmp_review.append(text_review[i].text)
        tmp_star_block.append(star_block_score[i].get_attribute('aria-label'))
        tmp_star_progress.append(star_progress_score[i].get_attribute('aria-label'))
        tmp_date.append(date[i].text)
        
        #수집한 1명의 리뷰를 결과 프레임에 추가
        #tmp_ID = pd.DataFrame(data=tmp_ID, columns="아이디", axis=1)
        #tmp_review = pd.DataFrame(data=tmp_review, columns="리뷰", axis=1)
        #tmp_star_block = pd.DataFrame(data=tmp_star_block, columns="별점- 상품", axis=1)
        #tmp_star_progress = pd.DataFrame(data=tmp_star_progress, columns="별점- 배송", axis=1)
        #tmp_date = pd.DataFrame(data=tmp_date, columns="날짜", axis=1)
        #data = pd.concat([data,tmp]) 
        
        review_dic = {
            "아이디": tmp_ID,
            "리뷰": tmp_review,
            "별점- 상품": tmp_star_block,
            "별점- 배송": tmp_star_progress,
            "날짜": tmp_date
            }


    print("티몬 호빵 리뷰 데이터 수집 완료", review_dic)
    
    return data

#스크롤 다운을 한 뒤, 크롤링을 해야 인덱스 에러가 발생하지 않음
scroll_down(driver, 275)
data = crawl(driver, data, 1364)

#인덱스 번호를 0부터 리셋
#data.reset_index(inplace=True, drop=True)
#data.head()

#데이터 저장
#tmp.to_csv('티몬_리뷰수집.csv', encoding='utf-8')
#tmp.to_exel('티몬_리뷰수집.xlsx')

#re=pd.read_csv('티몬_리뷰수집.csv', encoding='utf-8')
#re.head()