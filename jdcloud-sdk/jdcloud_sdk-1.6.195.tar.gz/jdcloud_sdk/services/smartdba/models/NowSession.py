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


class NowSession(object):

    def __init__(self, id=None, user=None, host=None, db=None, command=None, time=None, state=None, info=None):
        """
        :param id: (Optional) 会话id
        :param user: (Optional) 会话用户
        :param host: (Optional) 会话源端IP
        :param db: (Optional) 数据库
        :param command: (Optional) session命令
        :param time: (Optional) 会话活跃时间
        :param state: (Optional) 会话状态
        :param info: (Optional) 正在执行的sql
        """

        self.id = id
        self.user = user
        self.host = host
        self.db = db
        self.command = command
        self.time = time
        self.state = state
        self.info = info
