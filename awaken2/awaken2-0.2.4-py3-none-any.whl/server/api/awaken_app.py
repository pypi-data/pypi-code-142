# Copyright 2022 quinn.7@foxmail.com All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
[ AwakenApp ]

"""
from flask import Flask
from flask.blueprints import Blueprint

from ..api.blueprint import __all__ as blueprint_all
from ...baseic.keyword import G_KEYWORD
from ...baseic.broadcast.awaken_log import G_LOG
from ...baseic.common.configure import G_CONFIGURE
from ...baseic.decorator.baseic import deco_singleton


# --------------------------------------------------------------------------
@deco_singleton
class AwakenApp:
    """
    [ AwakenApp ]

    ---
    描述
    - 基于 Flask 实现的 Flask.WebApi 应用程序。

    """
    _app_living: Flask = Flask(__name__)
    """ 应用程序实例 """


    # ----------------------------------------------------------------------
    def __init__(self):
        self.update_config({'JSON_AS_ASCII': False})
        for blueprint in blueprint_all:
            self.load_blueprint(blueprint)


    # ----------------------------------------------------------------------
    @property
    def living(self) -> Flask:
        """ 
        [ 应用程序实例 ]

        ---
        返回
        - Flask : 返回应用程序实例。

        """
        return self._app_living


    # ----------------------------------------------------------------------
    def update_config(self, config_dict: dict) -> ...:
        """ 
        [ 更新配置项 ]

        ---
        描述
        - 更新 Flask 应用程序的配置项。

        ---
        参数
        - config_dict : { dict } - 配置项字典。

        """
        self._app_living.config.update(config_dict)

        if G_CONFIGURE.get(G_KEYWORD.Common.Config.Debug):
            for ck, cv in config_dict.items():
                G_LOG.info(f'{ self.__class__.__name__ } :: 更新配置 :: [{ ck } = { cv }]')


    # ----------------------------------------------------------------------
    def load_blueprint(self, blueprint: Blueprint) -> ...:
        """ 
        [ 载入蓝图 ]

        ---
        描述
        - 将蓝图对象载入 Flask 应用程序。

        ---
        参数
        - blueprint : { Blueprint } - Flask.Blueprint 蓝图对象。

        """
        self._app_living.register_blueprint(blueprint)

        if G_CONFIGURE.get(G_KEYWORD.Common.Config.Debug):
            G_LOG.info(f'{ self.__class__.__name__ } :: 载入蓝图 :: [{ blueprint }]')
