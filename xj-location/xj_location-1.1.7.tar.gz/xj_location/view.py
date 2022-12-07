# encoding: utf-8
"""
@project: djangoModel->api
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 逻辑拼装层
@created_time: 2022/5/31 17:21
"""
import json

from django.views.generic import View

from .models import Boundary, LocationGroup
from .services.location_info_service import LocationInfoService
from .utils.custom_response import *
from .validate import GroupValidate


def parse_data(data):
    # 解析request对象 请求参数
    requestData = {}
    for k, v in data.items():
        requestData[k] = v if not v == "" else None
    return requestData


# ================ 定位分组CURD =====================
class LocationGroupList(View):
    def get(self, request):
        service = LocationInfoService()
        return service.model_select(request, LocationGroup)


class LocationGroupCreate(View):
    def post(self, request):
        service = LocationInfoService()
        return service.model_create(request, LocationGroup, GroupValidate)


class LocationGroupDel(View):
    def post(self, request):
        service = LocationInfoService()
        return service.model_del(request, LocationGroup)


class LocationGroupUpdate(View):
    def post(self, request):
        service = LocationInfoService()
        return service.model_update(request, LocationGroup)

