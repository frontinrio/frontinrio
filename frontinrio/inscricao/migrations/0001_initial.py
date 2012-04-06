# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Inscricao'
        db.create_table('inscricao_inscricao', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('inscricao', ['Inscricao'])

        # Adding unique constraint on 'Inscricao', fields ['nome', 'email']
        db.create_unique('inscricao_inscricao', ['nome', 'email'])

    def backwards(self, orm):
        # Removing unique constraint on 'Inscricao', fields ['nome', 'email']
        db.delete_unique('inscricao_inscricao', ['nome', 'email'])

        # Deleting model 'Inscricao'
        db.delete_table('inscricao_inscricao')

    models = {
        'inscricao.inscricao': {
            'Meta': {'unique_together': "(('nome', 'email'),)", 'object_name': 'Inscricao'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['inscricao']