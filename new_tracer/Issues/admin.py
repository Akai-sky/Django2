from django.contrib import admin
from .models import IssuesType,Module,Issues,IssuesReply

# Register your models here.
admin.site.register(Module)
admin.site.register(Issues)
admin.site.register(IssuesType)
admin.site.register(IssuesReply)