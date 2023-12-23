from rest_framework import viewsets
from .models import FileRepository
from .serializers import FileRepositorySerializer, FileRepositorylistSerializer, FileFolderSerializer
from utils.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from .filters import File_folderFilter




class FileRepositoryViewSet(viewsets.ModelViewSet):
    queryset = FileRepository.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ('project', "parent")
    ordering_fields = ['file_type']

    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.action == "list":
            return FileRepositorylistSerializer
        return FileRepositorySerializer


class FileFolderViewSet(viewsets.ModelViewSet):
    queryset = FileRepository.objects.filter(file_type=2).order_by('id')
    serializer_class = FileFolderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('project','id','parent')
    pagination_class = PageNumberPagination
    # filterset_class = File_folderFilter



