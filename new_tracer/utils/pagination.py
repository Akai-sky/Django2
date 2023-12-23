"""
自定义分页器类
"""
from django.utils.translation import gettext_lazy as _
from rest_framework.pagination import PageNumberPagination as _PageNumberPagination


class PageNumberPagination(_PageNumberPagination):
    # 每页条数
    page_size = 8

    # 前端指定页码时可使用的查询字符串参数
    page_query_param = 'page'
    page_query_description = _('获取的页码.')

    # 前端指定每页数据条数时可使用的查询字符串参数
    page_size_query_param = 'size'
    page_size_query_description = _('每一页数据条数.')

    # 每页最大数据条数
    max_page_size = 50

    last_page_strings = ('last',)

    template = 'rest_framework/pagination/numbers.html'

    # 超过数据量时的提示
    invalid_page_message = _('无效页码.')