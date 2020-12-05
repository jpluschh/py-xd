#! /usr/bin/python3

import requests
from bs4 import BeautifulSoup

url = 'https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

for link in soup.find_all('text'):
    print(link.get('stockNo'))
