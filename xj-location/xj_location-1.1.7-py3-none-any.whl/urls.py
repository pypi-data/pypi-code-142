# encoding: utf-8

from django.urls import re_path

from .apis.boundary_api import BoundaryAPI
from .apis.group_api import GroupApi
from .apis.location_api import LocationAPI

# 应用名称
app_name = 'xj_location'

urlpatterns = [
    # 定位
    re_path('^add/?$', LocationAPI.as_view()),  # 创建定位
    re_path('^del/?(?P<id>\d+)?$', LocationAPI.as_view()),  # 删除定位
    re_path('^edit/?(?P<id>\d+)?$', LocationAPI.as_view()),  # 修改定位
    re_path('^list/?$', LocationAPI.list),  # 定位点 分页条件查询

    # 边界
    re_path('^boundary/?(?P<id>\d+)?$', BoundaryAPI.as_view()),
    re_path('^boundary_list/?$', BoundaryAPI.list),
    re_path('^boundary_is_contain/?$', BoundaryAPI.boundary_is_contain),  # 是否包含 定位点

    # # 分组
    re_path('^group_list/?$', GroupApi.as_view()),  # 获取分组数据

    re_path('^test/?$', LocationAPI.test),  # 获取分组数据
]
