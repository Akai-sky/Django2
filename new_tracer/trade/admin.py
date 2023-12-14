from django.contrib import admin

# Register your models here.
from .models import PricePolicy, Transaction

admin.site.register(PricePolicy)
admin.site.register(Transaction)