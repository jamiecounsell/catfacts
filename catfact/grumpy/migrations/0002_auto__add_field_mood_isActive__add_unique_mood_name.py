# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Mood.isActive'
        db.add_column(u'grumpy_mood', 'isActive',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding unique constraint on 'Mood', fields ['name']
        db.create_unique(u'grumpy_mood', ['name'])


    def backwards(self, orm):
        # Removing unique constraint on 'Mood', fields ['name']
        db.delete_unique(u'grumpy_mood', ['name'])

        # Deleting field 'Mood.isActive'
        db.delete_column(u'grumpy_mood', 'isActive')


    models = {
        u'grumpy.mood': {
            'Meta': {'object_name': 'Mood'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1600', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isActive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['grumpy']