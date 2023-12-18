from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import Wiki
from .serializers import WikiSerializer,WikiDetailSerializer


# Create your views here.
class WikiViewSet(viewsets.ModelViewSet):
    queryset = Wiki.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return WikiDetailSerializer
        elif self.action == "create":
            return WikiSerializer
        return WikiSerializer
    # #
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        ret = super().create(request, *args, **kwargs)
        return ret
    #     print('------------------111')
    #     # wiki_id = request.GET.get('wiki_id')
    #     # print(wiki_id)
    #     # serializer = self.get_serializer(data=request.data)
    #     # serializer.is_valid(raise_exception=True)
    #     #
    #     # serializer.validated_data["project_id"] = project_id
    #     # if serializer.validated_data["parent"]:
    #     #     serializer.validated_data["depth"] = serializer.validated_data["parent"]["depth"] + 1
    #     # else:
    #     #     serializer.validated_data["depth"] = 1
    #     # self.perform_create(serializer)
    #     # headers = self.get_success_headers(serializer.data)
    #     # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #     request.data._mutable = True
    #     request.data.update(project_id = project_id)
    #     request.data._mutable = False
    #
    #     print(project_id)
    #     print(request.data)
    #     print(request.POST)
    #     ret = super().create(request, *args, **kwargs)
    #     return ret
