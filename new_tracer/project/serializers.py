from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model
from .models import Project, ProjectUser
from trade.models import Transaction

import time
from datetime import datetime

User = get_user_model()


class ProjectSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, max_length=32,
                                 validators=[UniqueValidator(queryset=Project.objects.all(), message="项目名已存在")])
    creator = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    def validate_name(self, name):
        # userid = self.context["request"].userid
        # real_count = self.context["request"].price_policy.project_num
        userid = self.context["request"].user.id
        count = Project.objects.filter(creator_id=userid).count()

        _object = Transaction.objects.filter(user_id=userid, status=2).order_by('-id').first()
        current_datetime = datetime.now()
        if _object.end_datetime and _object.end_datetime < current_datetime:
            _object = Transaction.objects.filter(user_id=userid, status=2, price_policy__category=1).first()
        real_count = _object.price_policy.project_num
        if count >= real_count:
            raise serializers.ValidationError("项目个数超限，请购买套餐！")
        return name
    def create(self, validated_data):
        validated_data["bucket"] = "{}-{}-1231231231".format(self.context["request"].user.mobile, str(time.time()))
        validated_data["region"] = 'ap-guangzhou'
        instance = Project.objects.create(**validated_data)
        return instance

    class Meta:
        model = Project
        fields = ("name", "color", "desc", "creator")


class ProjectUserSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(many=False)

    class Meta:
        model = ProjectUser
        fields = "__all__"


class ProjectUserCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = ProjectUser
        fields = ("project", "user")


class ProjectStarSerializer(serializers.ModelSerializer):
    creator = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    def update(self, instance, validated_data):
        pro_obj = Project.objects.filter(id=instance.id).first()

    class Meta:
        model = Project
        fields = ("creator",)

class ProjectUserStarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectUser
        fields = "star"
