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


class UpdateUserRoomRequestObj(object):

    def __init__(self, userRoomId=None, roomName=None, roomType=None):
        """
        :param userRoomId: (Optional) 用户房间号
        :param roomName: (Optional) 房间名称
        :param roomType: (Optional) 房间类型 1-小房间；2-大房间
        """

        self.userRoomId = userRoomId
        self.roomName = roomName
        self.roomType = roomType
