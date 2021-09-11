import csv
from os import readlink
import requests
import time
from bs4 import BeautifulSoup
from soupsieve import select
import itertools

# yahooニュースにアクセス
res = requests.get('https://news.yahoo.co.jp/')
soup = BeautifulSoup(res.content, 'lxml')

# ベースとなるURL
# base_url = "https://news.yahoo.co.jp/"

ul_tag = soup.find_all('a',class_='sc-hmzhuo')
for tag in ul_tag:
  print(ul_tag)
  title = ul_tag[0].getText()
  print(title)
  url = ul_tag[0].get("href")
  print(url)

