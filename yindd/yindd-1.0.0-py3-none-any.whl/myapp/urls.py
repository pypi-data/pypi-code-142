"""clmapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from myapp.views import *
urlpatterns = [
    path("send_code/",Sms_CodeView.as_view()),
    path("login/",LoginView.as_view()),
    path("out_login/",LogoutView.as_view()),
    path("show_user/",Show_userInfo.as_view()),
    path("qntoken/", QNYtoken.as_view()),
    path("addresss/", ShowUser_address.as_view()),
    path("coupons/", Showuser_Coupon.as_view()),
    path("vip_list/", VipListView.as_view()),
    path("order/", Add_OrderView.as_view()),
    path("food/", Goods_PayView.as_view()),
    path("pay_notify/", PayNotifyView.as_view()),
    path("order_record/",OrderRecordView.as_view()),
    path("cates/",CateView.as_view()),
    path('addvip/',VipCreateView.as_view()),
    path('allvip/',VipAllView.as_view())

]
