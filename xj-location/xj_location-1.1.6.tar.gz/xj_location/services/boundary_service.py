# encoding: utf-8
"""
@project: djangoModel->boundary_service
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 边界服务
@created_time: 2022/9/7 14:10
"""
import json

from django.core.paginator import Paginator
from matplotlib.path import Path

from ..models import Boundary, Location
from ..utils.model_handle import format_params_handle


class BoundaryService:
    @staticmethod
    def boundary_list(params):
        params = format_params_handle(
            param_dict=params,
            filter_filed_list=["page", "size", "name", "id"],
            alias_dict={"name": "name__contains"}
        )
        page = params.pop("page", 1)
        size = params.pop("size", 20)
        location_set = Boundary.objects.filter(**params)
        count = location_set.count()
        location_set = location_set.values()
        finish_set = list(Paginator(location_set, size).page(page))
        return {"page": int(page), "size": int(size), "count": count, "list": finish_set}, None

    @staticmethod
    def add_boundary(params):
        params = format_params_handle(
            param_dict=params,
            filter_filed_list=["name", "boundary_list", "created_at"]
        )
        if not params:
            return None, "参数不能为空"
        instance = Boundary.objects.create(**params)
        return {"id": instance.id}, None

    @staticmethod
    def edit_boundary(params):
        params = format_params_handle(
            param_dict=params,
            filter_filed_list=["id", "name", "boundary_list", "created_at"]
        )
        id = params.pop("id", None)
        if not id:
            return None, "ID 不可以为空"
        if not params:
            return None, "没有可以修改的字段"
        instance = Boundary.objects.filter(id=id)
        if params:
            instance.update(**params)
        return None, None

    @staticmethod
    def del_boundary(id):
        if not id:
            return None, "ID 不可以为空"
        instance = Boundary.objects.filter(id=id)
        if instance:
            instance.delete()
        return None, None

    @staticmethod
    def boundary_contain_point(boundary_id, location_id):
        boundary_set = Boundary.objects.filter(id=boundary_id)
        point_set = Location.objects.filter(id=location_id)
        if not boundary_set:
            return None, "不存在该边界"
        if not point_set:
            return None, "不存在该定位点"
        try:
            boundary_list = boundary_set.first().to_json().get("boundary_list")
            boundary_list = json.loads(boundary_list)
            point_dict = point_set.first().to_json()
            # print(point_dict)
            # print(boundary_list)
            point = (float(point_dict['longitude']), float(point_dict['latitude']))
            p = Path(boundary_list)  # 加载边界
            is_contain = p.contains_point(point)  # 查询边界点
            return {"is_contain": is_contain}, None
        except Exception as e:
            return None, str(e)
