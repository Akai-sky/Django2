from rest_framework import serializers
from .models import Wiki


class WikiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wiki
        fields = ("project", "title", "content", "parent")

    def create(self, validated_data):
        project_id = validated_data["project"].id
        if validated_data["parent"]:
            parent = validated_data["parent"].id
            parent_wiki = Wiki.objects.filter(id=parent, project=project_id).first()
            depth = parent_wiki.depth + 1
        else:
            depth = 1
        validated_data["depth"] = depth
        instance = Wiki.objects.create(**validated_data)
        return instance


class WikiDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wiki
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        project_id = data["project"]
        parent = data["parent"]

        if parent:
            parent_wiki = Wiki.objects.filter(id=parent, project=project_id).first()
            parent_wiki_data = {}
            parent_wiki_data['project'] = parent_wiki.project_id
            parent_wiki_data['title'] = parent_wiki.title
            parent_wiki_data['content'] = parent_wiki.content
            parent_wiki_data['depth'] = parent_wiki.depth
            parent_wiki_data['parent'] = parent_wiki.parent_id
            data["wiki_parent"] = parent_wiki_data

        return data


class WikiCateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wiki
        fields = ("id", "title", "parent")
