import csv
from os import readlink
import requests
import time
from bs4 import BeautifulSoup
from soupsieve import select
import itertools

import soupsieve

# 愛知県防災情報 > 尾張西武のHTML要素を取得
res = requests.get('https://www.kasen-aichi.jp/RainfallHis_60_1_1.html?time=1631348662450')
bs = BeautifulSoup(res.content, 'lxml')

# ベースとなるURL
base_url = "https://www.kasen-aichi.jp/"

# 地域別URL取得
area_url = []
area = bs.select('#nav-list > li > a')
for a in area:
  href = a.get("href")
  area_url.append(base_url + href)



for a in area_url:
  res = requests.get(a)
  bs = BeautifulSoup(res.content, 'lxml')
  # 市町村名取得
  text = []
  table = bs.find("table")
  citys = table.select('tr > th > a')
  for city in citys:
    text.append(city.getText())
  print(text)
  # 詳細href取得、URL生成
  url =[]
  details = table.select('tr > th > div > a')
  for detail in details:
    href = detail.get("href")
    url.append(base_url + href)
  print(url)






  





