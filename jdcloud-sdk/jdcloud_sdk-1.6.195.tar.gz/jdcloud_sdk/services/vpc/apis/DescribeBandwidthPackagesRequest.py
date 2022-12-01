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


class DescribeBandwidthPackagesRequest(JDCloudRequest):
    """
    
查询共享带宽包列表

## 接口说明

- 使用 `filters` 过滤器进行条件筛选，每个 `filter` 之间的关系为逻辑与（AND）的关系。

- 如果使用子帐号查询，只会查询到该子帐号有权限的云主机实例。关于资源权限请参考 [IAM概述](https://docs.jdcloud.com/cn/iam/product-overview)。

- 单次查询最大可查询100条共享带宽包数据。

- 尽量一次调用接口查询多条数据，不建议使用该批量查询接口一次查询一条数据，如果使用不当导致查询过于密集，可能导致网关触发限流。

- 由于该接口为 `GET` 方式请求，最终参数会转换为 `URL` 上的参数，但是 `HTTP` 协议下的 `GET` 请求参数长度是有大小限制的，使用者需要注意参数超长的问题。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeBandwidthPackagesRequest, self).__init__(
            '/regions/{regionId}/bandwidthPackages/', 'GET', header, version)
        self.parameters = parameters


class DescribeBandwidthPackagesParameters(object):

    def __init__(self, regionId,):
        """
        :param regionId: Region ID
        """

        self.regionId = regionId
        self.pageNumber = None
        self.pageSize = None
        self.filters = None
        self.tags = None
        self.resourceGroupIds = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码, 默认为1, 取值范围：[1,∞), 页码超过总页数时, 显示最后一页
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小，默认为20，取值范围为[10,100]
        """
        self.pageSize = pageSize

    def setFilters(self, filters):
        """
        :param filters: (Optional) bwpIds - 共享带宽包ID，支持多个进行精确搜索
name - 共享带宽包名称，支持单个进行精确搜索

        """
        self.filters = filters

    def setTags(self, tags):
        """
        :param tags: (Optional) Tag筛选条件
        """
        self.tags = tags

    def setResourceGroupIds(self, resourceGroupIds):
        """
        :param resourceGroupIds: (Optional) 资源组筛选条件
        """
        self.resourceGroupIds = resourceGroupIds

