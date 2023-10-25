# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 23:48:36 2023

@author: nine5
"""
import requests
from bs4 import BeautifulSoup



url = 'https://www.esunbank.com/zh-tw/personal/deposit/rate/forex/foreign-exchange-rates'

header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }
data = requests.get(url,headers=header).text

soup = BeautifulSoup(data,'html.parser')

rates=soup.find(id='exchangeRate')


tbody=rates.find('tbody')
trs=tbody.find_all('tr')[1:]

for row in trs:
    tds=row.find_all('td',recursive=False)#  recursive遞迴搜尋, =False>>(關閉)
    if len (tds)==4:
        
        print(tds[0].text.split()[0].strip())  #.也可以寫成   .strip().split()[0]
        print(tds[1].text.strip())
        print(tds[2].text.strip())
        print(tds[3].text.strip())
        print()
        print()

