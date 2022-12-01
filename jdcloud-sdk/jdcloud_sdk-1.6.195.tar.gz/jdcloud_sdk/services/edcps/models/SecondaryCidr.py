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


class SecondaryCidr(object):

    def __init__(self, secondaryCidrId=None, cidr=None, region=None, az=None, subnetId=None, name=None, vpcId=None, vpcName=None, availableIpCount=None, totalIpCount=None):
        """
        :param secondaryCidrId: (Optional) 次要cidr的ID
        :param cidr: (Optional) 次要cidr
        :param region: (Optional) 地域代码, 如cn-east-tz1
        :param az: (Optional) 可用区, 如cn-east-tz1a
        :param subnetId: (Optional) 子网ID
        :param name: (Optional) 次要cidr名称
        :param vpcId: (Optional) 私有网络Id
        :param vpcName: (Optional) 私有网络名称
        :param availableIpCount: (Optional) 可用ip数量
        :param totalIpCount: (Optional) 总ip数量
        """

        self.secondaryCidrId = secondaryCidrId
        self.cidr = cidr
        self.region = region
        self.az = az
        self.subnetId = subnetId
        self.name = name
        self.vpcId = vpcId
        self.vpcName = vpcName
        self.availableIpCount = availableIpCount
        self.totalIpCount = totalIpCount
