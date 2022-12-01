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


class PauseLiveStreamTranslateRequest(JDCloudRequest):
    """
    暂停指定流的翻译任务
- 暂停添加实时翻译字幕到指定流
- 指定的流需在线且配置了翻译模板

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(PauseLiveStreamTranslateRequest, self).__init__(
            '/translate:pause', 'POST', header, version)
        self.parameters = parameters


class PauseLiveStreamTranslateParameters(object):

    def __init__(self, publishDomain, appName, streamName):
        """
        :param publishDomain: 推流域名
        :param appName: APP名
        :param streamName: 流名
        """

        self.publishDomain = publishDomain
        self.appName = appName
        self.streamName = streamName

