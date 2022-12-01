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


class KeyDetail(object):

    def __init__(self, keyId, keyName, keyVersionCount, keyVersionList, rotationCycle=None):
        """
        :param keyId:  KeyID
        :param keyName:  Key名称
        :param rotationCycle: (Optional) 轮换周期
        :param keyVersionCount:  Key版本的个数
        :param keyVersionList:  Key版本详情的列表
        """

        self.keyId = keyId
        self.keyName = keyName
        self.rotationCycle = rotationCycle
        self.keyVersionCount = keyVersionCount
        self.keyVersionList = keyVersionList
