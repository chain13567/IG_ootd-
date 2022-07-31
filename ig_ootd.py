from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
import pyautogui
from selenium.webdriver import ActionChains
from pynput.keyboard import Key, Controller
import pandas as pd
import requests
from selenium.webdriver.common.by import By
from pathlib import Path
import urllib 

def link():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(2)
    # 帳號
    driver.find_element_by_name("username").send_keys("帳號")
    # 密碼
    driver.find_element_by_name("password").send_keys("密碼")
    # 點擊登入
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
    # 等待時間
    time.sleep(4)
    # 設定開啟ootd
    driver.get("https://www.instagram.com/ootd_introducer/")
    # 等待時間
    time.sleep(2)
    # 建立link_list, 存放抓取的網頁 
    link_list = []
    # 網頁向下(1)
    for j in range(6):
        time.sleep(1.5)
        pyautogui.press('pgdn')
        # BeautifulSoup
        ootd_soup = BeautifulSoup(driver.page_source, 'html.parser')
        ootd_link = ootd_soup.find_all('a', {'class': 'oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl _a6hd'})
    
    for i in ootd_link:
        href_link = i.get('href')
        if 'p' in href_link:
            link_list.append(href_link)
    
    # print(link_list)
    # print(len(link_list))
    # 剔除最後一個explorer
    link_list.pop()
    # 網頁向下(2)
    for j in range(6):
        time.sleep(1.5)
        pyautogui.press('pgdn')
        # BeautifulSoup
        ootd_soup = BeautifulSoup(driver.page_source, 'html.parser')
        ootd_link = ootd_soup.find_all('a', {'class': 'oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl _a6hd'})
    
    for i in ootd_link:
        href_link = i.get('href')
        if 'p' in href_link:
            link_list.append(href_link)    
    link_list.pop()
    # 網頁向下(3)
    for j in range(6):
        time.sleep(1.5)
        pyautogui.press('pgdn')
        # BeautifulSoup
        ootd_soup = BeautifulSoup(driver.page_source, 'html.parser')
        ootd_link = ootd_soup.find_all('a', {'class': 'oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl _a6hd'})
    
    for i in ootd_link:
        href_link = i.get('href')
        if 'p' in href_link:
            link_list.append(href_link) 
    link_list.pop()        
    # 網頁向下(4)
    for j in range(6):
        time.sleep(1.5)
        pyautogui.press('pgdn')
        # BeautifulSoup
        ootd_soup = BeautifulSoup(driver.page_source, 'html.parser')
        ootd_link = ootd_soup.find_all('a', {'class': 'oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl _a6hd'})
    
    for i in ootd_link:
        href_link = i.get('href')
        if 'p' in href_link:
            link_list.append(href_link) 
    link_list.pop()        
    # 網頁向下(5)
    for j in range(6):
        time.sleep(1.5)
        pyautogui.press('pgdn')
        # BeautifulSoup
        ootd_soup = BeautifulSoup(driver.page_source, 'html.parser')
        ootd_link = ootd_soup.find_all('a', {'class': 'oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl _a6hd'})
    
    for i in ootd_link:
        href_link = i.get('href')
        if 'p' in href_link:
            link_list.append(href_link) 
    link_list.pop()
    # 網頁向下(6)
    for j in range(6):
        time.sleep(1.5)
        pyautogui.press('pgdn')
        # BeautifulSoup
        ootd_soup = BeautifulSoup(driver.page_source, 'html.parser')
        ootd_link = ootd_soup.find_all('a', {'class': 'oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl _a6hd'})
    
    for i in ootd_link:
        href_link = i.get('href')
        if 'p' in href_link:
            link_list.append(href_link) 
    link_list.pop()        
    # 網頁向下(7)
    for j in range(6):
        time.sleep(1.5)
        pyautogui.press('pgdn')
        # BeautifulSoup
        ootd_soup = BeautifulSoup(driver.page_source, 'html.parser')
        ootd_link = ootd_soup.find_all('a', {'class': 'oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl _a6hd'})
    
    for i in ootd_link:
        href_link = i.get('href')
        if 'p' in href_link:
            link_list.append(href_link)        
    link_list.pop()
    # 網頁向下(8)
    for j in range(6):
        time.sleep(1.5)
        pyautogui.press('pgdn')
        # BeautifulSoup
        ootd_soup = BeautifulSoup(driver.page_source, 'html.parser')
        ootd_link = ootd_soup.find_all('a', {'class': 'oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl _a6hd'})
    
    for i in ootd_link:
        href_link = i.get('href')
        if 'p' in href_link:
            link_list.append(href_link)
    link_list.pop()
    # 網頁向下(9)
    for j in range(6):
        time.sleep(1.5)
        pyautogui.press('pgdn')
        # BeautifulSoup
        ootd_soup = BeautifulSoup(driver.page_source, 'html.parser')
        ootd_link = ootd_soup.find_all('a', {'class': 'oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl _a6hd'})
    
    for i in ootd_link:
        href_link = i.get('href')
        if 'p' in href_link:
            link_list.append(href_link)
    link_list.pop()
    # 網頁向下(10)
    for j in range(6):
        time.sleep(1.5)
        pyautogui.press('pgdn')
        # BeautifulSoup
        ootd_soup = BeautifulSoup(driver.page_source, 'html.parser')
        ootd_link = ootd_soup.find_all('a', {'class': 'oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl _a6hd'})
    
    for i in ootd_link:
        href_link = i.get('href')
        if 'p' in href_link:
            link_list.append(href_link)
    # 剔除最後一個explorer
    link_list.pop()
    # 建立page_list, 存放處理後的網頁 
    page_list = []

    for a in range(len(link_list)):
        link = 'https://www.instagram.com/'+link_list[a]
        page_list.append(link)
    # print(page_list)
    # print(len(page_list))
    df = pd.DataFrame()
    df['網址'] = page_list
    df.to_csv('網址連結.csv', index=False, encoding='utf-8-sig')

# link()

# 創建存放內容的list
content_list = []
def get_content():
    # 登入
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(2)
    # 帳號
    driver.find_element_by_name("username").send_keys("帳號")
    # 密碼
    driver.find_element_by_name("password").send_keys("密碼")
    # 點擊登入
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
    # 等待時間
    time.sleep(4)
    df = pd.read_csv('網址連結.csv')
    link = list(df['網址'])
    for i in range(len(link)):
        driver.get(link[i])
        time.sleep(3)
        
        soup2 = BeautifulSoup(driver.page_source)
        content = soup2.find('div', {'class': '_a9zs'}).text
        # print(type(content))
        content_list.append(content)
        # print(content)
    df1 = pd.DataFrame()
    df1['內容'] = content_list
    df1.to_csv('內容.csv', index=False, encoding='utf-8-sig')
get_content()
