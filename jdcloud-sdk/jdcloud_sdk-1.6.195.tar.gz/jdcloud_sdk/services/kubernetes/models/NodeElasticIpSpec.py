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


class NodeElasticIpSpec(object):

    def __init__(self, bandWidthMbps, provider, chargeMode, ):
        """
        :param bandWidthMbps:  公网IP带宽【1-200】
        :param provider:  公网IP的provider：BGP
        :param chargeMode:  公网IP计费类型：flow流量计费,bandwith带宽计费
        """

        self.bandWidthMbps = bandWidthMbps
        self.provider = provider
        self.chargeMode = chargeMode
