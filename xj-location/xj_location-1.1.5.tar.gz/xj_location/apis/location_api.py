# encoding: utf-8
"""
@project: djangoModel->location_api
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis:
@created_time: 2022/9/7 13:27
"""

# ================ 定位操作 =====================
from rest_framework.views import APIView

from ..services.location_service import LocationService
from ..utils.model_handle import *


class LocationAPI(APIView):
    def list(self, **kwargs):
        # 用户组 列表接口
        params = parse_data(self)
        # 删除原来的权限判断，因为原来的权限呗重新写了，所以不可以使用了。
        # # auth_list = {}
        # # 权限判断
        # token = self.META.get('HTTP_AUTHORIZATION', None)
        # if token and str(token).strip().upper() != "BEARER":
        #     token_serv, error_text = UserService.check_token(token)
        #     if error_text:
        #         return util_response(err=6000, msg=error_text)
        #     token_serv, error_text = UserService.check_token(token)
        #     auth_list, error_text = PermissionService.get_user_group_permission(user_id=token_serv.get("user_id"), module="location")
        #     if error_text:
        #         return util_response(err=1002, msg=error_text)
        # auth_list = JDict(auth_list)
        # ban_user_list = []
        # allow_user_list = []
        # if auth_list.GROUP_PARENT and auth_list.GROUP_PARENT.ban_view.upper() == "Y":
        #     ban_user_list.extend(auth_list.GROUP_PARENT.user_list)
        # else:
        #     allow_user_list.extend(auth_list.GROUP_PARENT.user_list if auth_list.GROUP_PARENT else [])
        #
        # if auth_list.GROUP_CHILDREN and auth_list.GROUP_CHILDREN.ban_view.upper() == "Y":
        #     ban_user_list.extend(auth_list.GROUP_CHILDREN.user_list)
        # else:
        #     allow_user_list.extend(auth_list.GROUP_CHILDREN.user_list if auth_list.GROUP_CHILDREN else [])
        #
        # if auth_list.GROUP_INSIDE and auth_list.GROUP_INSIDE.ban_view.upper() == "Y":
        #     ban_user_list.extend(auth_list.GROUP_INSIDE.user_list)
        # else:
        #     allow_user_list.extend(auth_list.GROUP_INSIDE.user_list if auth_list.GROUP_INSIDE else [])
        #
        # if not auth_list.GROUP_ADMINISTRATOR and not auth_list.GROUP_MANAGER:
        #     if auth_list.GROUP_OUTSIDE and auth_list.GROUP_OUTSIDE.ban_view.upper() == "Y":
        #         params['user_id__in'] = allow_user_list
        #     else:
        #         params["user_id__not_in"] = ban_user_list
        data, err = LocationService.location_list(params)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)

    def put(self, request, **kwargs):
        # 用户组 编辑接口
        params = parse_data(request)
        params.setdefault("id", kwargs.get("id", None))
        data, err = LocationService.edit_location(params)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)

    def post(self, request, **kwargs):
        # 用户组 添加接口
        params = parse_data(request)
        data, err = LocationService.add_location(params)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)

    def delete(self, request, **kwargs):
        # 用户组 删除接口
        id = parse_data(request).get("id", None) or kwargs.get("id")
        if not id:
            return util_response(err=1000, msg="id 必传")
        data, err = LocationService.del_location(id)
        if err:
            return util_response(err=1001, msg=err)
        return util_response(data=data)

    def test(self):
        # 测试接口
        params = {"thread_id_list": [1, 2]}
        data, err = LocationService.location_list(params, False)
        return util_response(data=data)

