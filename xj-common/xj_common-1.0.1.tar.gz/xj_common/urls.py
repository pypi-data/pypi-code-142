from django.urls import re_path

from .api.translate_apis import TranslateApis

urlpatterns = [
    # 公共翻译
    re_path(r'^translate_article/?$', TranslateApis.translate_article, ),
    re_path(r'^translate_test/?$', TranslateApis.as_view(), ),
    # 公共定位服务
]
