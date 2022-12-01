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


class GetContainerLogsRequest(JDCloudRequest):
    """
    查询单个容器日志

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(GetContainerLogsRequest, self).__init__(
            '/regions/{regionId}/pods/{podId}/containers/{containerName}:getContainerLogs', 'GET', header, version)
        self.parameters = parameters


class GetContainerLogsParameters(object):

    def __init__(self, regionId,podId,containerName,):
        """
        :param regionId: Region ID
        :param podId: Pod ID
        :param containerName: container name
        """

        self.regionId = regionId
        self.podId = podId
        self.containerName = containerName
        self.tailLines = None
        self.sinceSeconds = None
        self.limitBytes = None
        self.startTime = None
        self.endTime = None

    def setTailLines(self, tailLines):
        """
        :param tailLines: (Optional) 返回日志文件中倒数 tailLines 行，如不指定，默认从容器启动时或 sinceSeconds 指定的时间读取。

        """
        self.tailLines = tailLines

    def setSinceSeconds(self, sinceSeconds):
        """
        :param sinceSeconds: (Optional) 返回相对于当前时间之前sinceSeconds之内的日志。

        """
        self.sinceSeconds = sinceSeconds

    def setLimitBytes(self, limitBytes):
        """
        :param limitBytes: (Optional) 限制返回的日志文件内容字节数，取值范围 [1-4]KB，最大 4KB.

        """
        self.limitBytes = limitBytes

    def setStartTime(self, startTime):
        """
        :param startTime: (Optional) 日志时间上限，不传表示不限时间

        """
        self.startTime = startTime

    def setEndTime(self, endTime):
        """
        :param endTime: (Optional) 日志时间下限，不传表示不限时间

        """
        self.endTime = endTime

