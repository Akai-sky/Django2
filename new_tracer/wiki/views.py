from rest_framework import mixins, viewsets
from .models import Wiki
from .serializers import WikiSerializer, WikiDetailSerializer, WikiCateSerializer
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from utils.pagination import PageNumberPagination
from rest_framework.response import Response


class WikiViewSet(viewsets.ModelViewSet):
    queryset = Wiki.objects.all()
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ('project',)
    pagination_class = PageNumberPagination
    ordering_fields = ['depth', 'id']

    def get_serializer_class(self):
        if self.action == "list":
            return WikiDetailSerializer
        elif self.action == "create":
            return WikiSerializer
        return WikiSerializer

    @action(
        detail=False,
        methods=['GET'],
        url_path='wiki_cate1',
        url_name='wiki_cate1'
    )
    def get_wiki_cate(self, request):
        wikilist = Wiki.objects.all().values("id", "title", "parent").order_by('depth', 'id')

        return Response(wikilist)

    @action(
        detail=False,
        methods=['POST'],
        url_path='wiki_upload',
        url_name='wiki_upload'
    )
    def create_wiki_upload(self, request, project_id):
        pass


class WikiCateViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Wiki.objects.all().order_by('depth', 'id')
    serializer_class = WikiCateSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('project',)
    pagination_class = PageNumberPagination
