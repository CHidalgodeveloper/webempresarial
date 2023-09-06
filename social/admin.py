from typing import Any, List, Optional, Tuple, Union
from django.contrib import admin
from django.http.request import HttpRequest
from .models import Social

# Register your models here.

class SocialAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

    def get_readonly_fields(self, request, obj:None):
        if request.user.groups.filter(name="Persoal").exists():
            return ('created','updated','key','name')

admin.site.register(Social, SocialAdmin)