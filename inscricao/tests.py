# -*- coding: utf-8 -*-

from django.test import TestCase

from inscricao.models import Inscricao, Checkout
from inscricao.forms import InscricaoForm

def inscricao_form(data):
    f = InscricaoForm(data)
    f.is_valid()
    return f


class BaseTestModelInscricao(TestCase):

    @classmethod
    def setUpClass(self):
        self.inscricao = Inscricao.objects.create(nome="Andre", email="teste@test.com")

    @classmethod
    def tearDownClass(self):
        self.inscricao.delete()

    def test_tem_campo_nome(self):
        self.assertEqual(self.inscricao.nome, 'Andre')

    def test_tem_campo_email(self):
        self.assertEqual(self.inscricao.email, 'teste@test.com')


class BaseTestModelCheckout(TestCase):

    @classmethod
    def setUpClass(self):
        self.inscricao = Inscricao.objects.create(nome="Andre", email="teste@test.com")
        self.checkout = Checkout.objects.create(codigo=1234, inscricao=self.inscricao)

    @classmethod
    def tearDownClass(self):
        self.inscricao.delete()
        self.checkout.delete()

    def test_tem_campo_codigo(self):
        self.assertEqual(self.checkout.codigo, 1234)

    def test_tem_campo_inscricao(self):
        self.assertEqual(self.checkout.inscricao, self.inscricao)

class TestFormInscricao(TestCase):

    def test_campos_excluidos_nao_devem_aparecer(self):
        form = InscricaoForm()
        self.assertNotIn('status', form.fields)
        self.assertNotIn('data_inscricao', form.fields)

    def test_campos_obrigatorios(self):
        form = inscricao_form({})
        self.assertIn('nome', form.errors)
        self.assertIn('cpf', form.errors)
        self.assertIn('email', form.errors)

    def test_validar_cpf_invalido(self):
        data = {'nome': 'andre fonseca', 'email':'test@gmail.com', 'cpf': '123123123-24'}
        form  = inscricao_form(data)
        self.assertIn('cpf', form.errors)

    def test_validar_cpf_valido(self):
        data = {'nome': 'andre fonseca', 'email':'test@gmail.com', 'cpf': '32844513743'}
        form  = inscricao_form(data)
        self.assertNotIn('cpf', form.errors)

