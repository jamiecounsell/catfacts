# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Fact'
        db.create_table(u'facts_fact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('body', self.gf('django.db.models.fields.TextField')(max_length=1600, blank=True)),
            ('isSample', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isSatire', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isApathetic', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isConcerned', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isNotCat', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isMythical', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'facts', ['Fact'])


    def backwards(self, orm):
        # Deleting model 'Fact'
        db.delete_table(u'facts_fact')


    models = {
        u'facts.fact': {
            'Meta': {'object_name': 'Fact'},
            'body': ('django.db.models.fields.TextField', [], {'max_length': '1600', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isApathetic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isConcerned': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isMythical': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isNotCat': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isSample': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isSatire': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['facts']