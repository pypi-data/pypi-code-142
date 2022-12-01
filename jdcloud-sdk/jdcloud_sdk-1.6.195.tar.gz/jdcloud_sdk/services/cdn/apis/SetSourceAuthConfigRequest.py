# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class SetSourceAuthConfigRequest(JDCloudRequest):
    """
    回源鉴权设置
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(SetSourceAuthConfigRequest, self).__init__(
            '/domain/{domain}/setSourceAuthConfig', 'POST', header, version)
        self.parameters = parameters


class SetSourceAuthConfigParameters(object):

    def __init__(self,domain, ):
        """
        :param domain: 用户域名
        """

        self.domain = domain
        self.enable = None
        self.originRole = None
        self.authType = None
        self.tosAuthInfo = None
        self.ossAuthInfo = None

    def setEnable(self, enable):
        """
        :param enable: (Optional) 是否开启鉴权[on,off]
        """
        self.enable = enable

    def setOriginRole(self, originRole):
        """
        :param originRole: (Optional) 回源为主/备[master,slave]
        """
        self.originRole = originRole

    def setAuthType(self, authType):
        """
        :param authType: (Optional) 鉴权类型[oss,aws,tos],aws暂不支持
        """
        self.authType = authType

    def setTosAuthInfo(self, tosAuthInfo):
        """
        :param tosAuthInfo: (Optional) tos类型鉴权参数,authType为tos是不能为空
        """
        self.tosAuthInfo = tosAuthInfo

    def setOssAuthInfo(self, ossAuthInfo):
        """
        :param ossAuthInfo: (Optional) oss类型鉴权参数,authType为oss是不能为空
        """
        self.ossAuthInfo = ossAuthInfo

