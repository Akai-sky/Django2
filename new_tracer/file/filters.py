import django_filters
from django.db.models import Q

from .models import FileRepository


class File_folderFilter(django_filters.rest_framework.FilterSet):
    folder_id = django_filters.NumberFilter(method='recursion_folder_filter')

    #     def recursion_folder_filter(self, queryset, name, value):
    #         breadcrumb_list = []
    #         parent_object = queryset.filter(id=int(value))
    #         while parent_object:
    #             breadcrumb_list.insert(0, model_to_dict(FileRepository, ['id', 'name']))
    #             parent_object = parent_object.get('parent')
    #
    #             print('parent_object',parent_object)
    # #     breadcrumb_list [{'id': 2, 'name': '草莓'},
    #         #              {'id': 3, 'name': '草莓'},
    #         #              {'id': 4, 'name': '草莓'}]
    #         return breadcrumb_list
    def recursion_folder_filter(self, queryset, name, value):
        # if
        return queryset.filter(Q(id=value) | Q(parent=value))
        # net = ret.child.all()
        # print('net',net)
        # print(type(net))


    class Meta:
        model = FileRepository
        fields = ["folder_id"]
