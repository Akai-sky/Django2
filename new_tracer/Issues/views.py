from rest_framework import viewsets
from .models import IssuesType,Module,Issues,IssuesReply
from .serializers import IssuesSerializer, ModuleSerializer,IssuesReplySerializer, IssuesTypeSerializer
from utils.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class IssuesViewSet(viewsets.ModelViewSet):
    queryset = Issues.objects.all()
    serializer_class = IssuesSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ['assign', 'attention']
    filterset_fields = ('priority',"status",'issues_type')
    pagination_class = PageNumberPagination


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    filter_backends = [DjangoFilterBackend]
    pagination_class = PageNumberPagination


class IssuesReplyViewSet(viewsets.ModelViewSet):
    queryset = IssuesReply.objects.all()
    serializer_class = IssuesReplySerializer
    filter_backends = [DjangoFilterBackend]
    pagination_class = PageNumberPagination


class IssuesTypeViewSet(viewsets.ModelViewSet):
    queryset = IssuesType.objects.all()
    serializer_class = IssuesTypeSerializer
    filter_backends = [DjangoFilterBackend]
    pagination_class = PageNumberPagination