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


class DisableInternetAccessRequest(JDCloudRequest):
    """
    关闭TiDB服务的公网访问域名
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DisableInternetAccessRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}:disableInternetAccess', 'POST', header, version)
        self.parameters = parameters


class DisableInternetAccessParameters(object):

    def __init__(self,regionId, instanceId, serviceType):
        """
        :param regionId: 地域代码
        :param instanceId: 实例ID
        :param serviceType: 按照service type (database pd monitor)关闭公网域名
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.serviceType = serviceType

