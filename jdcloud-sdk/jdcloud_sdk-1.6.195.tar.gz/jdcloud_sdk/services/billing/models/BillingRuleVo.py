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


class BillingRuleVo(object):

    def __init__(self, id=None, site=None, appCode=None, appCodeName=None, serviceCode=None, serviceCodeName=None, pin=None, strategy=None, strategyName=None, cycleType=None, cycleTypeName=None, dosingMode=None, dosingCycle=None, billingMode=None, timeSpan=None, isDeleted=None, operator=None, createTime=None, updateTime=None):
        """
        :param id: (Optional) id
        :param site: (Optional) 站点
        :param appCode: (Optional) 业务线编码
        :param appCodeName: (Optional) 业务线名称
        :param serviceCode: (Optional) 产品编码
        :param serviceCodeName: (Optional) 产品编码名称
        :param pin: (Optional) 用户pin
        :param strategy: (Optional) 计费时长类型 - 0:按使用时长；1:按周期时长
        :param strategyName: (Optional) 计费时长类型名称
        :param cycleType: (Optional) 计费周期类型 - 0:按小时；1:按天
        :param cycleTypeName: (Optional) 计费周期类型名称
        :param dosingMode: (Optional) 区分大客户 - 1:是；0:否
        :param dosingCycle: (Optional) 大客户统计周期 - 0:按小时计费；1:按天计费
        :param billingMode: (Optional) 计费模式 - 1:删除不计费；2:关机不计费
        :param timeSpan: (Optional) 最小计费时长 - 必须为大于等于0的整数
        :param isDeleted: (Optional) 删除状态 - 0:未删除；1:已删除
        :param operator: (Optional) 操作人
        :param createTime: (Optional) 创建时间
        :param updateTime: (Optional) 修改时间
        """

        self.id = id
        self.site = site
        self.appCode = appCode
        self.appCodeName = appCodeName
        self.serviceCode = serviceCode
        self.serviceCodeName = serviceCodeName
        self.pin = pin
        self.strategy = strategy
        self.strategyName = strategyName
        self.cycleType = cycleType
        self.cycleTypeName = cycleTypeName
        self.dosingMode = dosingMode
        self.dosingCycle = dosingCycle
        self.billingMode = billingMode
        self.timeSpan = timeSpan
        self.isDeleted = isDeleted
        self.operator = operator
        self.createTime = createTime
        self.updateTime = updateTime
