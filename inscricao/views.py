# -*- coding: utf-8 -*-
import logging
import requests

from lxml import etree

from django.views.generic.base import View
from django.template import response
from django.conf import settings

from .forms import InscricaoForm
from .models import Checkout

logger = logging.getLogger('frontinrio.inscricoes')

class InscricaoView(View):

    def gerar_cobranca(self, inscricao):
        headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
        payload = settings.PAGSEGURO
        payload["itemAmount1"] = "%.2f" % 40
        payload["reference"] = "%s" % inscricao.pk
        response = requests.post(settings.PAGSEGURO_CHECKOUT, data=payload, headers=headers)
        if response.ok:
            dom = etree.fromstring(response.content)
            codigo_checkout = dom.xpath("//code")[0].text
            return codigo_checkout
        else:
            logger.error("\n\n\n########## Erro na inscrição do participante %d - %s (%s) ##########" % (inscricao.pk, inscricao.nome, inscricao.email))
            logger.error("Erro na comunicação com PagSeguro: %s - %s" % (response.status_code, response.content))
            logger.error("#################################################################\n\n\n")
            return None

    def enviar_email_sucesso(self):
        pass

    def get(self, request):
        context = {'form': InscricaoForm()}
        return response.TemplateResponse(request, 'inscricao.html', context)

    def post(self, request):
        form = InscricaoForm(request.POST)
        if form.is_valid():
            form.save()
            inscricao =  form.instance
            codigo_checkout = self.gerar_cobranca(inscricao)
            if codigo_checkout:
                checkout = Checkout.objects.create(codigo=codigo_checkout, inscricao=inscricao)
                self.enviar_email_sucesso(checkout)
                context = {'inscricao': inscricao }
                return response.TemplateResponse(request, 'sucesso.html', context)

        context = {"form": form}
        return response.TemplateResponse(request, 'inscricao.html', context)


