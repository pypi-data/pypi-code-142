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


class IpResource(object):

    def __init__(self, region=None, resourceType=None, ip=None, bandwidth=None, cleanThresholdBps=None, cleanThresholdPps=None, blackHoleThreshold=None, instanceId=None, instanceName=None, instanceType=None, safeStatus=None):
        """
        :param region: (Optional) 公网 IP 所在区域编码
        :param resourceType: (Optional) 公网 IP 类型或绑定资源类型. 
<br>- 0: 未知类型
<br>- 1: 弹性公网 IP(IP 为弹性公网 IP, 绑定资源类型未知)
<br>- 10: 弹性公网 IP(IP 为弹性公网 IP, 但未绑定资源)
<br>- 11: 云主机
<br>- 12: 负载均衡
<br>- 13: 原生容器实例
<br>- 14: 原生容器 Pod
<br>- 2: 云物理服务器公网 IP
<br>- 3: Web应用防火墙公网 IP
<br>- 4: 托管区公网 IP"

        :param ip: (Optional) 公网 IP 地址
        :param bandwidth: (Optional) 带宽上限, 单位 Mbps
        :param cleanThresholdBps: (Optional) 每秒请求流量
        :param cleanThresholdPps: (Optional) 每秒报文请求数
        :param blackHoleThreshold: (Optional) 黑洞阈值
        :param instanceId: (Optional) 绑定防护包 ID, 为空字符串时表示未绑定防护包
        :param instanceName: (Optional) 绑定防护包名称, 为空字符串时表示未绑定防护包
        :param instanceType: (Optional) 套餐类型, 为 0 时未绑定防护包. <br>- 1: 独享 IP<br>- 2: 共享 IP
        :param safeStatus: (Optional) 安全状态. <br>- 0: 安全<br>- 1: 清洗<br>- 2: 黑洞
        """

        self.region = region
        self.resourceType = resourceType
        self.ip = ip
        self.bandwidth = bandwidth
        self.cleanThresholdBps = cleanThresholdBps
        self.cleanThresholdPps = cleanThresholdPps
        self.blackHoleThreshold = blackHoleThreshold
        self.instanceId = instanceId
        self.instanceName = instanceName
        self.instanceType = instanceType
        self.safeStatus = safeStatus
