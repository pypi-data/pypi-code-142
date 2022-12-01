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


class PutPoint(object):

    def __init__(self, metric, resourceId, timestamp, value, tags=None):
        """
        :param metric:  监控指标名称，长度不超过255字节，只允许英文、数字、下划线_、点.,  [0-9][a-z] [A-Z] [. _ ]， 其它会返回err
        :param resourceId:  资源的唯一表示，一般为uuid
        :param tags: (Optional) 数据维度，数据类型为map类型，最多五个标签，尽量不传或少传。总长度不大于255字节，只允许英文、数字、下划线_、点., [0-9][a-z] [A-Z] [. _ ]，  其它会返回err
        :param timestamp:  秒级时间戳，早于当前时间30天的不能写入；建议的上报时间戳：上报时间间隔的整数倍，如上报间隔为5s，则建议上报的时间戳为 timestamp = current timestamp - (current timestamp % time interval) = 1487647187 - （1487647187 % 5） = 1487647187 -2 = 1487647185
        :param value:  监控的值。number。最大值为long.MAX_VALUE=9223372036854775807=263-1。累计类型的指标，累计到最大值后需要翻转为0，重新开始计数。翻转后不影响速率的计算。
        """

        self.metric = metric
        self.resourceId = resourceId
        self.tags = tags
        self.timestamp = timestamp
        self.value = value
