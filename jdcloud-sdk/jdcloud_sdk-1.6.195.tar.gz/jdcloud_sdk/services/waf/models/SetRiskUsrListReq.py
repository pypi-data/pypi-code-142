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


class SetRiskUsrListReq(object):

    def __init__(self, wafInstanceId, domain, name, desc, disable, id=None, rules=None, bz64File=None):
        """
        :param id: (Optional) 规则id,新增时传0
        :param wafInstanceId:  WAF实例id
        :param domain:  域名
        :param name:  规则名称
        :param desc:  desc
        :param disable:  0-使用中 1-禁用
        :param rules: (Optional) 策略规则, 格式：["13311112222","13211112222"]
        :param bz64File: (Optional) 自定义名单上传文件内容,base64编码
        """

        self.id = id
        self.wafInstanceId = wafInstanceId
        self.domain = domain
        self.name = name
        self.desc = desc
        self.disable = disable
        self.rules = rules
        self.bz64File = bz64File
