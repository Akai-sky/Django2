from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins, viewsets, authentication
# Create your views here.
from .serializers import ProjectSerializer, ProjectUserSerializer, ProjectUserCreateSerializer, ProjectStarSerializer
from .models import Project, ProjectUser

from .filters import ProjectsFilter
from django.contrib.auth import get_user_model


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('star',)
    # filterset_class = ProjectsFilter
    permission_classes = (IsAuthenticated,)
    # permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)
    authentication_classes = (authentication.SessionAuthentication,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        return Project.objects.filter(creator=self.request.user)


class ProjectUserViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):
    queryset = ProjectUser.objects.all()
    filter_backends = [DjangoFilterBackend]
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.SessionAuthentication,)
    filterset_fields = ('star',)

    def get_serializer_class(self):
        if self.action == "list":
            return ProjectUserSerializer
        elif self.action == "create":
            return ProjectUserCreateSerializer
        return ProjectUserCreateSerializer

    def get_queryset(self):
        return ProjectUser.objects.filter(user=self.request.user)


class ProjectStarViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin,
                         viewsets.GenericViewSet):
    "项目收藏"
    queryset = Project.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectStarSerializer
    lookup_field = "id"
    # def update(self, request, *args, **kwargs):
    #     # star = request.data["name"]
    #     partial = kwargs.pop('partial', False)
    #
    #     print("star",request.data)
    #     instance = self.get_object()
    #
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #
    #     # request.data["star"] = star
    #     # return super().update(request, *args, **kwargs)
    #     return Response(serializer.data)

    def get_queryset(self):
        return Project.objects.filter(creator=self.request.user)
