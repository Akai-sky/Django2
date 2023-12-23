from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser


class userProfile(AbstractUser):
    """
    用户
    """
    name = models.CharField(max_length=30, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女")), default="female")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(max_length=10)
    mobile = models.CharField(max_length=11)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
