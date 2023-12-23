from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import FileRepository


User = get_user_model()



class FileFolderSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=32)
    update_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = FileRepository
        fields = ("id", "project", "name", "parent", "update_user")


    def validate_name(self, name):
        name = name
        project = self.initial_data["project"]
        parent = self.initial_data["parent"]
        queryset = FileRepository.objects.filter(file_type=2, name=name, project=project)
        if parent:
            exists = queryset.filter(parent=parent).exists()
        else:
            exists = queryset.filter(parent__isnull=True).exists()
        if exists:
            raise serializers.ValidationError("文件夹已存在！")
        return name

    def create(self, validated_data):
        validated_data["file_type"] = 2
        instance = FileRepository.objects.create(**validated_data)
        return instance


class FileRepositorySerializer(serializers.ModelSerializer):
    update_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = FileRepository
        fields = ("project", "file_type", "name", "file_path", "parent", "update_user")


class FileRepositorylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileRepository
        fields = "__all__"
