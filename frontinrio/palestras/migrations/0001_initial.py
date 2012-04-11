# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Palestra'
        db.create_table('palestras_palestra', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('descricao', self.gf('django.db.models.fields.TextField')()),
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('minicv', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('avatar', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('palestras', ['Palestra'])

    def backwards(self, orm):
        # Deleting model 'Palestra'
        db.delete_table('palestras_palestra')

    models = {
        'palestras.palestra': {
            'Meta': {'object_name': 'Palestra'},
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minicv': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['palestras']