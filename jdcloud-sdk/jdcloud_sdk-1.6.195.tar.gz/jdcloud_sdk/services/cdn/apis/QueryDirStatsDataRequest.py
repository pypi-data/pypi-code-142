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


class QueryDirStatsDataRequest(JDCloudRequest):
    """
    查询目录基础统计数据，仅有部分用户支持该功能
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(QueryDirStatsDataRequest, self).__init__(
            '/statistics:queryDirStatsData', 'POST', header, version)
        self.parameters = parameters


class QueryDirStatsDataParameters(object):

    def __init__(self,):
        """
        """

        self.startTime = None
        self.endTime = None
        self.domain = None
        self.dirs = None
        self.cacheType = None

    def setStartTime(self, startTime):
        """
        :param startTime: (Optional) 查询起始时间,UTC时间，格式为:yyyy-MM-dd'T'HH:mm:ss'Z'，示例:2018-10-21T10:00:00Z
        """
        self.startTime = startTime

    def setEndTime(self, endTime):
        """
        :param endTime: (Optional) 查询截止时间,UTC时间，格式为:yyyy-MM-dd'T'HH:mm:ss'Z'，示例:2018-10-21T10:00:00Z
        """
        self.endTime = endTime

    def setDomain(self, domain):
        """
        :param domain: (Optional) 需要查询的域名, 必须为用户pin下有权限的域名，该接口仅支持单域名查询
        """
        self.domain = domain

    def setDirs(self, dirs):
        """
        :param dirs: (Optional) 需要过滤的目录
        """
        self.dirs = dirs

    def setCacheType(self, cacheType):
        """
        :param cacheType: (Optional) 查询节点层级，可选值:[all,edge,mid],默认查询all,edge边缘 mid中间
        """
        self.cacheType = cacheType

