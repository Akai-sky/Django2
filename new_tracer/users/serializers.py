import uuid
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model

from .models import VerifyCode
from trade.models import PricePolicy,Transaction
from datetime import datetime, timedelta

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "birthday", "gender", "mobile", "email")


class UserRegSerializer(serializers.ModelSerializer):
    username = serializers.CharField(label="用户名", required=True, allow_blank=False,
                                     validators=[
                                         UniqueValidator(queryset=User.objects.filter(), message="用户名已经存在")])
    email = serializers.EmailField(label="邮箱", required=True, allow_blank=False,
                                   validators=[
                                       UniqueValidator(queryset=User.objects.all(), message="用户名已经存在")])
    mobile = serializers.CharField(label="手机号", required=True, allow_blank=False,
                                   validators=[
                                       UniqueValidator(queryset=User.objects.all(), message="用户名已经存在")])
    password = serializers.CharField(style={'input_type': "password"}, label="密码", write_only=True)
    confirm_password = serializers.CharField(style={'input_type': "password"}, label="确认密码",
                                             write_only=True)
    code = serializers.CharField(required=True, write_only=True, max_length=4, min_length=4, label="验证码",
                                 error_messages={
                                     "blank": "请输入验证码",
                                     "required": "请输入验证码",
                                     "max_length": "验证码格式错误",
                                     "min_length": "验证码格式错误",
                                 })


    def validate_code(self, code):
        verify_record = VerifyCode.objects.filter(mobile=self.initial_data["mobile"]).order_by("-add_time")
        if verify_record:
            last_record = verify_record[0]

            five_min_age = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
            if five_min_age > last_record.add_time:
                raise serializers.ValidationError("验证码过期")

            if last_record.code != code:
                raise serializers.ValidationError("验证码错误")
        else:
            raise serializers.ValidationError("验证码错误")


    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        print("user",user)
        print(user.id)
        policy_object = PricePolicy.objects.filter(category=1,title="Free").first()
        Transaction.objects.create(
            status=2,
            order=str(uuid.uuid4()),
            user=user,
            price_policy=policy_object,
            count=0,
            price=0,
            start_datetime=datetime.now()
        )
        return user

    def validate(self, attrs):
        del attrs["code"]
        del attrs["confirm_password"]
        return attrs

    class Meta:
        model = User
        fields = ("username", "email", "mobile", "password", "confirm_password", "code")
