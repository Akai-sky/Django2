from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Wiki

from datetime import datetime


class WikiSerializer(serializers.ModelSerializer):


    def create(self, validated_data):
        print('------')
        # print(self.context["request"].project_id)
        print('1111')
        print(validated_data)
        wiki = Wiki.objects.create(**validated_data)

        return wiki

    class Meta:
        model = Wiki
        fields = ("project_id", "title", "content", "parent")


class WikiDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wiki
        fields = "__all__"
