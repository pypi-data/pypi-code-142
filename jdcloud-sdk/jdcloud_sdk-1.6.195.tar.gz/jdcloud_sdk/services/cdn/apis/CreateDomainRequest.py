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


class CreateDomainRequest(JDCloudRequest):
    """
    创建点播加速域名
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateDomainRequest, self).__init__(
            '/domain/{domain}', 'POST', header, version)
        self.parameters = parameters


class CreateDomainParameters(object):

    def __init__(self,domain, ):
        """
        :param domain: 用户域名
        """

        self.domain = domain
        self.sourceType = None
        self.cdnType = None
        self.backSourceType = None
        self.dailyBandWidth = None
        self.quaility = None
        self.maxFileSize = None
        self.minFileSize = None
        self.sumFileSize = None
        self.avgFileSize = None
        self.defaultSourceHost = None
        self.httpType = None
        self.ipSource = None
        self.domainSource = None
        self.ossSource = None
        self.accelerateRegion = None
        self.tempInstId = None
        self.domainCnameTag = None

    def setSourceType(self, sourceType):
        """
        :param sourceType: (Optional) 回源类型只能是[ips,domain,oss]中的一种
        """
        self.sourceType = sourceType

    def setCdnType(self, cdnType):
        """
        :param cdnType: (Optional) 点播域名的类型只能是[vod,download,web]中的一种
        """
        self.cdnType = cdnType

    def setBackSourceType(self, backSourceType):
        """
        :param backSourceType: (Optional) 回源方式,只能是[https,http]中的一种,默认http
        """
        self.backSourceType = backSourceType

    def setDailyBandWidth(self, dailyBandWidth):
        """
        :param dailyBandWidth: (Optional) 日带宽(Mbps)
        """
        self.dailyBandWidth = dailyBandWidth

    def setQuaility(self, quaility):
        """
        :param quaility: (Optional) 服务质量,只能是[good,general]中的一种,默认为good
        """
        self.quaility = quaility

    def setMaxFileSize(self, maxFileSize):
        """
        :param maxFileSize: (Optional) 
        """
        self.maxFileSize = maxFileSize

    def setMinFileSize(self, minFileSize):
        """
        :param minFileSize: (Optional) 
        """
        self.minFileSize = minFileSize

    def setSumFileSize(self, sumFileSize):
        """
        :param sumFileSize: (Optional) 
        """
        self.sumFileSize = sumFileSize

    def setAvgFileSize(self, avgFileSize):
        """
        :param avgFileSize: (Optional) 
        """
        self.avgFileSize = avgFileSize

    def setDefaultSourceHost(self, defaultSourceHost):
        """
        :param defaultSourceHost: (Optional) 
        """
        self.defaultSourceHost = defaultSourceHost

    def setHttpType(self, httpType):
        """
        :param httpType: (Optional) 
        """
        self.httpType = httpType

    def setIpSource(self, ipSource):
        """
        :param ipSource: (Optional) 
        """
        self.ipSource = ipSource

    def setDomainSource(self, domainSource):
        """
        :param domainSource: (Optional) 
        """
        self.domainSource = domainSource

    def setOssSource(self, ossSource):
        """
        :param ossSource: (Optional) 
        """
        self.ossSource = ossSource

    def setAccelerateRegion(self, accelerateRegion):
        """
        :param accelerateRegion: (Optional) 加速区域:(mainLand:中国大陆，nonMainLand:海外加港澳台，all:全球)默认为中国大陆
        """
        self.accelerateRegion = accelerateRegion

    def setTempInstId(self, tempInstId):
        """
        :param tempInstId: (Optional) 
        """
        self.tempInstId = tempInstId

    def setDomainCnameTag(self, domainCnameTag):
        """
        :param domainCnameTag: (Optional) cname标签,使用时通过queryDomainCnameTag接口获取
        """
        self.domainCnameTag = domainCnameTag

