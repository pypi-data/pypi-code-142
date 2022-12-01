#!/usr/bin/env python
from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination

from drfcommon.response import done


class ComPagination(PageNumberPagination):
    """
    自定义分页器
    """
    page_size = 5
    page_size_query_param = 'pagesize'
    max_page_size = 50

    def get_paginated_response(self, data, page_key='data'):
        page_data = OrderedDict([
            ('count', self.page.paginator.count),
            ('page', self.page.number),
            # 总页数量
            ('pages', self.page.paginator.num_pages),
            # 每页数量
            ('pagesize', self.get_page_size(self.request)),
            ('lists', data)
        ])
        if page_key:
            page_map = {
                page_key: page_data
            }
            return done(**page_map)
        return done(**page_data)
