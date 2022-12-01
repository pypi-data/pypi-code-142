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


class DescribeSlowLogsRequest(JDCloudRequest):
    """
    查询MySQL实例的慢日志的概要信息。<br>- 仅支持MySQL
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeSlowLogsRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/performance:describeSlowLogs', 'GET', header, version)
        self.parameters = parameters


class DescribeSlowLogsParameters(object):

    def __init__(self, regionId, instanceId, startTime, endTime, ):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        :param instanceId: RDS 实例ID，唯一标识一个RDS实例
        :param startTime: 慢日志开始时间，格式为：YYYY-MM-DD HH:mm:ss，开始时间到当前时间不能大于 7 天，开始时间不能大于结束时间，结束时间不能大于当前时间
        :param endTime: 慢日志结束时间，格式为：YYYY-MM-DD HH:mm:ss，开始时间到当前时间不能大于 7 天，开始时间不能大于结束时间，结束时间不能大于当前时间
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.startTime = startTime
        self.endTime = endTime
        self.dbName = None
        self.pageNumber = None
        self.pageSize = None
        self.filters = None
        self.sorts = None

    def setDbName(self, dbName):
        """
        :param dbName: (Optional) 查询哪个数据库的慢日志，不填表示返回所有数据库的慢日志
        """
        self.dbName = dbName

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 显示数据的页码，默认为1，取值范围：[-1,1000)。pageNumber为-1时，返回所有数据页码；超过总页数时，显示最后一页。
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 每页显示的数据条数，默认为10，取值范围：10、20、30、50、100
        """
        self.pageSize = pageSize

    def setFilters(self, filters):
        """
        :param filters: (Optional) 
        """
        self.filters = filters

    def setSorts(self, sorts):
        """
        :param sorts: (Optional) 排序参数，支持rowsExaminedSum、rowsSentSum、lockTimeSum、executionCount、executionTimeSum
        """
        self.sorts = sorts

