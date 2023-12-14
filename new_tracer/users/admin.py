from django.contrib import admin

# Register your models here.
from .models import userProfile, VerifyCode


admin.site.register(userProfile)
admin.site.register(VerifyCode)