from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins, viewsets, authentication
from .serializers import ProjectSerializer, ProjectUserSerializer, ProjectUserCreateSerializer, ProjectStarSerializer, \
    ProjectUserStarSerializer
from .models import Project, ProjectUser
from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ('star',)
    ordering_fields = ['id']
    permission_classes = (IsAuthenticated,)
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
    lookup_field = 'project_id'

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

    def get_queryset(self):
        return Project.objects.filter(creator=self.request.user)


class ProjectUserStarViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin,
                             viewsets.GenericViewSet):
    "参与的项目收藏"
    queryset = ProjectUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectUserStarSerializer
    lookup_field = 'project_id'

    def get_queryset(self):
        return ProjectUser.objects.filter(user=self.request.user)


class AllProjectViewSet(ObjectMultipleModelAPIViewSet):
    "所有涉及项目"

    def get_querylist(self):
        queryset = [
            {'queryset': Project.objects.filter(creator=self.request.user),
             'serializer_class': ProjectSerializer},
            {'queryset': ProjectUser.objects.filter(user=self.request.user),
             'serializer_class': ProjectUserSerializer, 'lookup_field': 'project_id'},
        ]

        return queryset
