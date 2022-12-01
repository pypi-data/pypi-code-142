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


class ChangeHTTP2EdgePrioritizationSettingRequest(JDCloudRequest):
    """
    HTTP/2边缘优化，优化了通过HTTP/2提供的资源交付，提高了页面加载性能。当与Worker结合使用时，它还支持对内容交付的精细控制。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ChangeHTTP2EdgePrioritizationSettingRequest, self).__init__(
            '/zones/{zone_identifier}/settings$$h2_prioritization', 'PATCH', header, version)
        self.parameters = parameters


class ChangeHTTP2EdgePrioritizationSettingParameters(object):

    def __init__(self, zone_identifier, ):
        """
        :param zone_identifier: 
        """

        self.zone_identifier = zone_identifier
        self.value = None

    def setValue(self, value):
        """
        :param value: (Optional) 该设置的有效值
        """
        self.value = value

