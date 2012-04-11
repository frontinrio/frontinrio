# -*- coding: utf-8 -*-
from django.contrib import admin

from palestras.models import Palestra


class PalestraAdmin(admin.ModelAdmin):
    pass


admin.site.register(Palestra, PalestraAdmin)

