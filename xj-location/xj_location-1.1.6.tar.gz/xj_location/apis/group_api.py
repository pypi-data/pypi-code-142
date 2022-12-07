# encoding: utf-8
"""
@project: djangoModel->group_api
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis:
@created_time: 2022/9/7 15:05
"""
from rest_framework.views import APIView

from xj_location.models import LocationGroup
from ..utils.model_handle import model_select


# 临时接口
class GroupApi(APIView):
    def get(self, request):
        return model_select(request, LocationGroup)
