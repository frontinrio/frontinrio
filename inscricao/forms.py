# -*- coding: utf-8 -*-
from django import forms
from django.contrib.localflavor.br.forms import BRCPFField

from .models import Inscricao

class InscricaoForm(forms.ModelForm):
    cpf= BRCPFField()

    class Meta:
        model  = Inscricao
        exclude = ['status']

    def clean_nome(self):
        value = self.cleaned_data['nome']

        palavras = value.split()
        if len(palavras) <=1:
            raise forms.ValidationError(u'Insira o nome completo')

        return value

