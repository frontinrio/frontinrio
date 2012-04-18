# -*- coding: utf-8 -*-
from django.test import TestCase
from django.db import models

from palestras.models import Palestra

class TestPalestraModel(TestCase):

    def setUp(self):
        self.nome_campos = Palestra._meta.get_all_field_names()

    def test_model_tem_campo_titulo(self):
        self.assertIn('titulo', self.nome_campos)

    def test_model_tem_campo_descricao(self):
        self.assertIn('descricao', self.nome_campos)

    def test_model_tem_campo_autor(self):
        self.assertIn('autor', self.nome_campos)

    def test_model_tem_campo_minicv(self):
        self.assertIn('minicv', self.nome_campos)

    def test_model_tem_campo_avatar(self):
        self.assertIn('avatar', self.nome_campos)

class TestTiposCamposPalestraModel(TestCase):

    def test_campo_avatar_tipo_imagem(self):
        self.assertIsInstance(Palestra._meta.get_field_by_name('avatar')[0], models.ImageField)
