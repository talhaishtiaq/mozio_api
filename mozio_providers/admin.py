from django.contrib import admin

# Register your models here.
from .models import Provider, Jeojson


admin.site.register(Provider)
admin.site.register(Jeojson)
