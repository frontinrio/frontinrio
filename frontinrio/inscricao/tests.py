# -*- coding: utf-8 -*-

from django.test import TestCase

from inscricao.models import Inscricao


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



