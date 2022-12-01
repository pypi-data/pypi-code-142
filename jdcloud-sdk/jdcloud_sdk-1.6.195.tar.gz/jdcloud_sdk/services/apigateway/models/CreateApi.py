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


class CreateApi(object):

    def __init__(self, apiGroupId, apiName, action, path, matchType, reqBodyType, backServiceConfig, description=None, reqParams=None, reqBody=None, resBody=None, resBodyType=None, apiBackendConfig=None, backServiceType=None, backServicePath=None, backServiceId=None, backServiceName=None, backUrl=None, backServiceVersion=None, hufuAppTypeId=None, editableReqBodyType=None, editableResBodyType=None):
        """
        :param apiGroupId:  分组ID
        :param apiName:  名称
        :param action:  动作
        :param path:  请求路径
        :param matchType:  匹配模式：1."absolute"(绝对匹配); 2."prefix"（前缀匹配）;
        :param description: (Optional) 描述
        :param reqParams: (Optional) 请求参数列表
        :param reqBody: (Optional) 请求格式
        :param resBody: (Optional) 返回格式
        :param reqBodyType:  请求格式类型,1:application/json,2:text/xml,3:其他
        :param resBodyType: (Optional) 返回格式类型,1:application/json,2:text/xml,3:其他
        :param apiBackendConfig: (Optional) api后端配置
        :param backServiceType: (Optional) 后端服务类型，如HTTP/HTTPS,mock,funcion等
        :param backServicePath: (Optional) 后端服务地址，如后端服务地址，funtion路径等
        :param backServiceId: (Optional) 后端服务ID，如函数ID等
        :param backServiceName: (Optional) 后端服务名称，如函数名称
        :param backUrl: (Optional) 后端地址
        :param backServiceConfig:  后端服务配置，为true时，采用与分组统一的配置，初始创建api时请设置为True。
        :param backServiceVersion: (Optional) 后端服务版本，如函数版本名称
        :param hufuAppTypeId: (Optional) 应用类型ID,云鼎业务线专用
        :param editableReqBodyType: (Optional) 请求格式类型,当reqBodyType等于3时,使用该请求格式类型
        :param editableResBodyType: (Optional) 响应格式类型,当resBodyType等于3时,使用该响应格式类型
        """

        self.apiGroupId = apiGroupId
        self.apiName = apiName
        self.action = action
        self.path = path
        self.matchType = matchType
        self.description = description
        self.reqParams = reqParams
        self.reqBody = reqBody
        self.resBody = resBody
        self.reqBodyType = reqBodyType
        self.resBodyType = resBodyType
        self.apiBackendConfig = apiBackendConfig
        self.backServiceType = backServiceType
        self.backServicePath = backServicePath
        self.backServiceId = backServiceId
        self.backServiceName = backServiceName
        self.backUrl = backUrl
        self.backServiceConfig = backServiceConfig
        self.backServiceVersion = backServiceVersion
        self.hufuAppTypeId = hufuAppTypeId
        self.editableReqBodyType = editableReqBodyType
        self.editableResBodyType = editableResBodyType
