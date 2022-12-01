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


class QueryRefreshTaskRequest(JDCloudRequest):
    """
    查询刷新预热任务
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(QueryRefreshTaskRequest, self).__init__(
            '/task', 'GET', header, version)
        self.parameters = parameters


class QueryRefreshTaskParameters(object):

    def __init__(self,):
        """
        """

        self.startTime = None
        self.endTime = None
        self.keyword = None
        self.taskId = None
        self.taskStatus = None
        self.taskType = None
        self.pageNumber = None
        self.pageSize = None
        self.accountType = None
        self.subUsers = None

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

    def setKeyword(self, keyword):
        """
        :param keyword: (Optional) url或者目录的模糊查询关键字
        """
        self.keyword = keyword

    def setTaskId(self, taskId):
        """
        :param taskId: (Optional) 任务id
        """
        self.taskId = taskId

    def setTaskStatus(self, taskStatus):
        """
        :param taskStatus: (Optional) null
        """
        self.taskStatus = taskStatus

    def setTaskType(self, taskType):
        """
        :param taskType: (Optional) null
        """
        self.taskType = taskType

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 分页页数,默认值1
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页页面大小,默认值50
        """
        self.pageSize = pageSize

    def setAccountType(self, accountType):
        """
        :param accountType: (Optional) 查询的账号范围
        """
        self.accountType = accountType

    def setSubUsers(self, subUsers):
        """
        :param subUsers: (Optional) 查询的子账号，多个用逗号隔开
        """
        self.subUsers = subUsers

