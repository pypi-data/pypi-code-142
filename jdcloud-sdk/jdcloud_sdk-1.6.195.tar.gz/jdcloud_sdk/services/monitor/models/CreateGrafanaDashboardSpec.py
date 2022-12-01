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


class CreateGrafanaDashboardSpec(object):

    def __init__(self, params, templateUid, title, description=None, folderId=None):
        """
        :param description: (Optional) 
        :param folderId: (Optional) FolderId，文件夹id，默认为0
        :param params:  Params, 模板参数名称及指定值，key为名称、value为指定值
        :param templateUid:  templateUid
        :param title:  Title
        """

        self.description = description
        self.folderId = folderId
        self.params = params
        self.templateUid = templateUid
        self.title = title
