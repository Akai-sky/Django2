import django_filters

from .models import Project


class ProjectsFilter(django_filters.rest_framework.FilterSet):
    """
    项目
    """
    class Meta:
        model = Project
        fields = ['star']
