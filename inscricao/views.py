# -*- coding: utf-8 -*-
from django.views.generic.base import View
from django.template import response

from .forms import InscricaoForm


class InscricaoView(View):

    def get(self, request):
        context = {'form': InscricaoForm()}
        return response.TemplateResponse(request, 'inscricao.html', context)

    def post(self, request):
        form = InscricaoForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'inscricao': form.instance}
            return response.TemplateResponse(request, 'sucesso.html', context)

        context = {"form": form}
        return response.TemplateResponse(request, 'inscricao.html', context)


