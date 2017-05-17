from django.contrib import admin

# Register your models here.

from .models import RawURL
admin.site.register(RawURL)  # register index model so that we can use it in admin panel