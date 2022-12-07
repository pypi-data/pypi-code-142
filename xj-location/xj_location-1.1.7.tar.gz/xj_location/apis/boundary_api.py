# encoding: utf-8
"""
@project: djangoModel->boundary_api
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 边界API
@created_time: 2022/9/7 14:06
"""
from rest_framework.views import APIView

from ..services.boundary_service import BoundaryService
from ..utils.custom_response import util_response
from ..utils.model_handle import parse_data


class BoundaryAPI(APIView):
    def list(self, **kwargs):
        # 用户组 列表接口
        params = parse_data(self)
        data, err = BoundaryService.boundary_list(params)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)

    def put(self, request, **kwargs):
        # 用户组 添加接口
        params = parse_data(request)
        params.setdefault("id", kwargs.get("id", None))
        data, err = BoundaryService.edit_boundary(params)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)

    def post(self, request, **kwargs):
        # 用户组 修改接口
        params = parse_data(request)
        data, err = BoundaryService.add_boundary(params)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)

    def delete(self, request, **kwargs):
        # 用户组 删除接口
        id = parse_data(request).get("id", None) or kwargs.get("id")
        if not id:
            return util_response(err=1000, msg="id 必传")
        data, err = BoundaryService.del_boundary(id)
        if err:
            return util_response(err=1001, msg=err)
        return util_response(data=data)

    def boundary_is_contain(self, **kwargs):
        params = parse_data(self)
        location_id = params.get('location_id')
        boundary_id = params.get('boundary_id')
        if not location_id or not boundary_id:
            return util_response(err=1000, msg="参数错误")
        data, err = BoundaryService.boundary_contain_point(boundary_id, location_id)
        if err:
            return util_response(err=1001, msg=err)
        return util_response(data=data)
