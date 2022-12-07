# encoding: utf-8
"""
@project: djangoModel->location_service
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 定位服务
@created_time: 2022/9/7 13:38
"""
from django.core.paginator import Paginator
from django.db.models import Q

from ..models import Location
from ..utils.model_handle import format_params_handle


class LocationService:

    @staticmethod
    def location_list(params, need_pagination=True, fields=None):
        # 支持其他服务调用
        if not need_pagination:
            params = format_params_handle(
                param_dict=params,
                filter_filed_list=["region_code", "thread_id_list", "group_id_list", "thread_id", "group_id"],
                alias_dict={"name": "name__contains", "thread_id_list": "thread_id__in", "group_id_list": "group_id__in"}
            )
            if not params:
                return [], None
            try:
                location_obj = Location.objects.filter(**params)
            except Exception as e:
                return None, str(e)
            if not location_obj:
                return [], None
            if fields:
                return list(location_obj.values(*fields)), None

            return list(location_obj.values()), None

        # 正常分页查询
        params = format_params_handle(
            param_dict=params,
            filter_filed_list=["page", "size", "region_code", "name", "user_id", "by_user_id", "group_id", "user_id__in", "user_id__not_in"],
            alias_dict={"name": "name__contains"}
        )
        page = params.pop("page", 1)
        size = params.pop("size", 20)
        # 权限非判断
        location_obj = Location.objects
        if params.get("user_id__not_in"):
            location_obj = location_obj.filter(~Q(user_id__in=params.pop("user_id__not_in")))
        location_obj = location_obj.filter(**params)
        count = location_obj.count()
        location_set = location_obj.values()
        if fields:
            location_set = location_obj.values(*fields)
        finish_set = list(Paginator(location_set, size).page(page))

        return {"page": int(page), "size": int(size), "count": count, "list": finish_set}, None

    @staticmethod
    def add_location(params):
        params = format_params_handle(
            param_dict=params,
            filter_filed_list=[
                "region_code", "name", "address", "coordinate_type", "longitude", "latitude",
                "altitude", "user_id", "by_user_id", "group_id", "created_time", "category_id", "classify_id"
            ]
        )
        if not params:
            return None, "参数不能为空"
        instance = Location.objects.create(**params)
        return {"id": instance.id}, None

    @staticmethod
    def edit_location(params):
        params = format_params_handle(
            param_dict=params,
            filter_filed_list=[
                "id", "region_code", "name", "address", "coordinate_type", "longitude",
                "latitude", "altitude", "user_id", "by_user_id", "group_id", "created_time",
                "category_id", "classify_id"
            ]
        )
        id = params.pop("id", None)
        if not id:
            return None, "ID 不可以为空"
        if not params:
            return None, "没有可以修改的字段"
        instance = Location.objects.filter(id=id)
        if params:
            instance.update(**params)
        return None, None

    @staticmethod
    def del_location(id):
        if not id:
            return None, "ID 不可以为空"
        instance = Location.objects.filter(id=id)
        if instance:
            instance.delete()
        return None, None
