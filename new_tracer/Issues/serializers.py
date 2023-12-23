from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import IssuesType, Module, Issues, IssuesReply

User = get_user_model()


class IssuesTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssuesType
        fields = "__all__"


class IssuesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issues
        fields = "__all__"




class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = "__all__"


class IssuesReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = IssuesReply
        fields = "__all__"
