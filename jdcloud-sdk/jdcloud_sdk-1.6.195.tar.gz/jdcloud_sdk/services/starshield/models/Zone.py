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


class Zone(object):

    def __init__(self, plan_pending=None, original_dnshost=None, permissions=None, development_mode=None, verification_key=None, plan=None, original_name_servers=None, name=None, account=None, activated_on=None, paused=None, status=None, owner=None, modified_on=None, created_on=None, ty_pe=None, id=None, name_servers=None, original_registrar=None):
        """
        :param plan_pending: (Optional) 
        :param original_dnshost: (Optional) 切换到星盾时的DNS主机
        :param permissions: (Optional) 当前用户在域上的可用权限
        :param development_mode: (Optional) 域的开发模式过期（正整数）或上次过期（负整数）的时间间隔（秒）。如果从未启用过开发模式，则此值为0。

        :param verification_key: (Optional) 
        :param plan: (Optional) 
        :param original_name_servers: (Optional) 迁移到星盾之前的原始域名服务器
        :param name: (Optional) 域名
        :param account: (Optional) 
        :param activated_on: (Optional) 最后一次检测到所有权证明和该域激活的时间
        :param paused: (Optional) 指示域是否仅使用星盾DNS服务。如果值为真，则表示该域将不会获得安全或性能方面的好处。
        :param status: (Optional) 域的状态
        :param owner: (Optional) 
        :param modified_on: (Optional) 上次修改域的时间
        :param created_on: (Optional) 创建域的时间
        :param ty_pe: (Optional) 全接入的域意味着DNS由星盾托管。半接入的域通常是合作伙伴托管的域或CNAME设置。
        :param id: (Optional) 域标识符标签
        :param name_servers: (Optional) 星盾分配的域名服务器。这仅适用于使用星盾DNS的域
        :param original_registrar: (Optional) 切换到星盾时的域注册商
        """

        self.plan_pending = plan_pending
        self.original_dnshost = original_dnshost
        self.permissions = permissions
        self.development_mode = development_mode
        self.verification_key = verification_key
        self.plan = plan
        self.original_name_servers = original_name_servers
        self.name = name
        self.account = account
        self.activated_on = activated_on
        self.paused = paused
        self.status = status
        self.owner = owner
        self.modified_on = modified_on
        self.created_on = created_on
        self.ty_pe = ty_pe
        self.id = id
        self.name_servers = name_servers
        self.original_registrar = original_registrar
