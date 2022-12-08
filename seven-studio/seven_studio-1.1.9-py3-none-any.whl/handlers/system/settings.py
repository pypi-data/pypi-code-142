# -*- coding: utf-8 -*-
"""
:Author: ChenXiaolei
:Date: 2020-12-09 19:11:51
:LastEditTime: 2022-12-08 10:13:51
:LastEditors: HuangJingCan
:Description: 
"""

from seven_studio.handlers.studio_base import *
from seven_studio.models.db_models.settings.settings_base_model import *


class BaseSettingsHandler(StudioBaseHandler):
    @login_filter(True)
    def post_async(self):
        """
        :description: 设置站点基础信息
        :return 基础信息
        :last_editors: ChenXiaolei
        """
        login_background = self.get_param("login_background")
        login_logo = self.get_param("login_logo")
        banner_logo = self.get_param("banner_logo")
        title = self.get_param("title")
        login_expire = int(self.get_param("login_expire", 2))

        settings_base_model = SettingsBaseModel(config.get_value("manage_context_key"))

        settings_base = settings_base_model.get_entity()

        if not settings_base:
            settings_base = SettingsBase()

        settings_base.login_background = login_background
        settings_base.login_logo = login_logo
        settings_base.banner_logo = banner_logo
        settings_base.title = title
        settings_base.login_expire = login_expire

        if settings_base.id > 0:
            settings_base_model.update_entity(settings_base)
        else:
            settings_base_model.add_entity(settings_base)

        if config.get_value("login_type") == "redis":
            redis_init = self.redis_init()
            settings_base = redis_init.delete("settings_base")

        return self.response_json_success(settings_base)

    def get_async(self):
        """
        :description: 获取站点基础信息
        :return 基础信息
        :last_editors: ChenXiaolei
        """
        settings_base_model = SettingsBaseModel(config.get_value("manage_context_key"))

        settings_base = None
        if config.get_value("login_type") == "redis":
            redis_init = self.redis_init()
            settings_base = redis_init.get("settings_base")
            if not settings_base:
                settings_base = settings_base_model.get_dict()
                redis_init.set("settings_base", self.json_dumps(settings_base))
            else:
                settings_base = self.json_loads(settings_base)
        else:
            settings_base = settings_base_model.get_dict()

        return self.response_json_success(settings_base)