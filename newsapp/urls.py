#path関数をインポート
from django.urls import path
#ビューの設定ファイルをインポート
from . import views

app_name = 'newsapp'

#ルーティング
urlpatterns = [
    # localhost:8000/newsapp
    path('', views.Create.as_view(), name='home'),
    path('list/', views.list, name='list'),
    # localhost:8000/newsapp/keito
    path('test', views.test, name='test'),
    path('aichi', views.aichi, name='aichi'),
]
