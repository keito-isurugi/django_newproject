"""newsproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#管理ページ用のオブジェクトをインポート
from newsapp import views
from django.contrib import admin
#ルーティング用の関数をインポート
from django.urls import path, include

#ルーティングの内容をリストに記載
urlpatterns = [
    path('admin/', admin.site.urls),
    path('newsapp/', include('newsapp.urls')),
    path('test/', views.test ,name='test'),
    path('aichi/', views.aichi ,name='aichi'),
    # path('list/', views.list ,name='list'),
]
