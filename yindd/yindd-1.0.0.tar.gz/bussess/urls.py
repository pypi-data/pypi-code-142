"""takes URL Configuration

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
from django.contrib import admin
from django.urls import path
from bussess.views import *
urlpatterns = [
    # 获取手机验证码接口
    path('sms/<str:mobile>/',SmsView.as_view()),
    # 图片验证码的接口
    path("image_code/<str:uuid>/", ImageCodeAPIView.as_view()),
    # 手机号验证码登入
    path('login/',UserView.as_view()),
    # 商品的获取和添加
    path('classify/',ClassifyView.as_view()),
    # 商品的编辑和删除
    path('classify/<int:id>/',ClassifyInfoView.as_view()),


]
