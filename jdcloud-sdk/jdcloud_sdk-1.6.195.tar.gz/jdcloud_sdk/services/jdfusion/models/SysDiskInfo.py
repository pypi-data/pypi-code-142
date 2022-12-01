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


class SysDiskInfo(object):

    def __init__(self, diskSize=None, diskMediumType=None, diskName=None, autoDelete=None, status=None):
        """
        :param diskSize: (Optional) 硬盘大小
        :param diskMediumType: (Optional) 磁盘介质分类，目前为预留，可以为空
        :param diskName: (Optional) 磁盘名称
        :param autoDelete: (Optional) 磁盘是否随主机一起删除
        :param status: (Optional) 磁盘状态
        """

        self.diskSize = diskSize
        self.diskMediumType = diskMediumType
        self.diskName = diskName
        self.autoDelete = autoDelete
        self.status = status
