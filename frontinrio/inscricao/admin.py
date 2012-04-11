# -*- coding: utf-8 -*-
from django.contrib import admin

from inscricao.models import Inscricao

class InscricaoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Inscricao, InscricaoAdmin)
