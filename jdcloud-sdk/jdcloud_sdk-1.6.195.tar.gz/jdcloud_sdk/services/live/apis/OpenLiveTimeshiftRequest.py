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


class OpenLiveTimeshiftRequest(JDCloudRequest):
    """
    开启时移
直播支持最大4小时的HLS时移，使用方式为在播放域名后增加时移参数来实现，参数类型支持指定开始时间和时间偏移量2种方式进行时移。 开启直播时移后，重新推流生效，使用播放域名带相应参数访问即可播放
- 域名格式：
1、http://{playDomain}/{appName}/{streamName}/index.m3u8?timeshift=400（秒，指从当前时间往前时移的偏移量）
2、http://{playDomain}/{appName}/{streamName}/index.m3u8?starttime=1529223702 (unix时间戳)

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(OpenLiveTimeshiftRequest, self).__init__(
            '/liveTimeshift:open', 'PUT', header, version)
        self.parameters = parameters


class OpenLiveTimeshiftParameters(object):

    def __init__(self, playDomain):
        """
        :param playDomain: 直播的播放域名
        """

        self.playDomain = playDomain

