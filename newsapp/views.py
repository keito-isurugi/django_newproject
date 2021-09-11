from django.shortcuts import render
from .models import News
from django.views.generic import CreateView
from django.urls import reverse_lazy
import urllib.request
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse


class Create(CreateView):
   template_name = 'home.html'
   model = News
   fields = ('url',)
   success_url = reverse_lazy('list')


def list(request):
   for post in News.objects.all():
      url = post.url
   list = []
   response = requests.get(url)
   bs = BeautifulSoup(response.text, "html.parser")
   ul_tag = bs.find_all('a', class_='sc-hmzhuo')
   for tag in ul_tag:
      title = tag.getText()
      url2 = tag.get("href")
      list.append([title, url2])
   context = {'list': list, }
   return render(request, 'list.html', context)

def test(request):
   context = {
       'message': '初めてのメッセージ',
       'content': 'ようこそ、Djangoは楽しい！',
   }
   return render(request, 'test.html', context)


def aichi(request):
   list = []
   response = requests.get('https://www.kasen-aichi.jp/RainfallHis_60_1_1.html?time=1631348643457')
   bs = BeautifulSoup(response.content, "html.parser")

   # ベースとなるURL
   base_url = "https://www.kasen-aichi.jp/"

   # 県名取得
   text = []
   table = bs.find("table")
   prefs = table.select('tr > th > a')
   for pref in prefs:
      text.append(pref.getText())

   # 詳細href取得、URL生成
   url = []
   details = table.select('tr > th > div > a')
   for detail in details:
      href = detail.get("href")
      url.append(base_url + href)

   # 県名とURLをlistに追加しcontextに代入
   for t, u in zip(text, url):
      list.append([t, u])
   context = {'list': list, }
   return render(request, 'aichi.html', context)
