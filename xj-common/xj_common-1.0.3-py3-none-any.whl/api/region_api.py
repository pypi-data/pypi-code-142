# encoding: utf-8
"""
@project: djangoModel->region_api
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis:
@created_time: 2022/12/6 10:56
"""
import json
from time import time

from django.core import serializers
from django.http import JsonResponse
from django.views import View
from django.views.decorators.http import require_http_methods

from ..models import Region
from ..services.public_service import parse_data, model_del
from ..services.regin_service import RegionService
from ..validate import RegionValidate


# =============== 地区操作 =======================
class RegionList(View):
    # 查询列表
    @require_http_methods(["GET"])
    def get_child_region(self, code):
        # 获取下级的行政地区，0获取省级
        res_set = Region.objects.filter(p_code=code, is_delete=0)
        res_set = json.loads(serializers.serialize('json', res_set))
        final_res_dict = []
        for i in res_set:
            final_res_dict.append(i['fields'])
        return JsonResponse({'isSuccess': True, 'msg': '加载成功', 'data': final_res_dict})

    @require_http_methods(["GET"])
    def get_tree_region(self):
        start_time = time()
        service = RegionService()
        region_tree = service.tree_lock_loop()
        end_time = time()
        return JsonResponse({'run_time': end_time - start_time, 'isSuccess': True, 'msg': '加载成功', 'data': region_tree})


class RegionCreate(View):
    # 添加操作
    def post(self, request):
        data = parse_data(request.POST)
        validator = RegionValidate(data)
        is_valid, error = validator.validate()
        if not is_valid:
            return JsonResponse({'isSuccess': False, 'msg': error})
        res = Region.objects.filter(code=data['code'], is_delete=0)
        if res:
            return JsonResponse({'isSuccess': False, 'msg': '该数据已存在'})
        Region.objects.create(**data)
        return JsonResponse({'isSuccess': True, 'msg': '添加成功', 'data': ''})


class RegionUpdate(View):
    # 地区修改
    def post(self, request):
        id = request.POST.get('id')
        if not id:
            return JsonResponse({'isSuccess': False, 'msg': 'ID 必传'})
        data = parse_data(request.POST)
        res_obj = Region.objects.filter(id=id, is_delete=0)
        if not res_obj:
            return JsonResponse({'isSuccess': False, 'msg': '该数据不存在'})
        del data['id']
        res_obj.update(**data)
        return JsonResponse({'isSuccess': True, 'msg': '修改成功', 'data': ''})


class RegionDel(View):
    # 删除地区
    def post(self, request):
        res = model_del(request, Region, True)
        return JsonResponse(res)


class RegionCodeParse(View):

    def parse_code(self, code):
        # 解析code
        service = RegionService()
        res = service.cn_parse_location_code(code)
        return JsonResponse({'isSuccess': True, 'msg': '加载成功', 'data': res})
