# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Mood'
        db.create_table(u'grumpy_mood', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=1600, blank=True)),
        ))
        db.send_create_signal(u'grumpy', ['Mood'])


    def backwards(self, orm):
        # Deleting model 'Mood'
        db.delete_table(u'grumpy_mood')


    models = {
        u'grumpy.mood': {
            'Meta': {'object_name': 'Mood'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1600', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['grumpy']