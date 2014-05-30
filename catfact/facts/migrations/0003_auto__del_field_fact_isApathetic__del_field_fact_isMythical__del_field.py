# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Fact.isApathetic'
        db.delete_column(u'facts_fact', 'isApathetic')

        # Deleting field 'Fact.isMythical'
        db.delete_column(u'facts_fact', 'isMythical')

        # Deleting field 'Fact.isConcerned'
        db.delete_column(u'facts_fact', 'isConcerned')

        # Deleting field 'Fact.isSatire'
        db.delete_column(u'facts_fact', 'isSatire')

        # Deleting field 'Fact.isNotCat'
        db.delete_column(u'facts_fact', 'isNotCat')

        # Deleting field 'Fact.isSample'
        db.delete_column(u'facts_fact', 'isSample')

        # Adding M2M table for field mood on 'Fact'
        m2m_table_name = db.shorten_name(u'facts_fact_mood')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('fact', models.ForeignKey(orm[u'facts.fact'], null=False)),
            ('mood', models.ForeignKey(orm[u'grumpy.mood'], null=False))
        ))
        db.create_unique(m2m_table_name, ['fact_id', 'mood_id'])


    def backwards(self, orm):
        # Adding field 'Fact.isApathetic'
        db.add_column(u'facts_fact', 'isApathetic',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Fact.isMythical'
        db.add_column(u'facts_fact', 'isMythical',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Fact.isConcerned'
        db.add_column(u'facts_fact', 'isConcerned',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Fact.isSatire'
        db.add_column(u'facts_fact', 'isSatire',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Fact.isNotCat'
        db.add_column(u'facts_fact', 'isNotCat',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Fact.isSample'
        db.add_column(u'facts_fact', 'isSample',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Removing M2M table for field mood on 'Fact'
        db.delete_table(db.shorten_name(u'facts_fact_mood'))


    models = {
        u'facts.fact': {
            'Meta': {'object_name': 'Fact'},
            'body': ('django.db.models.fields.TextField', [], {'max_length': '1600', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mood': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['grumpy.Mood']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'grumpy.mood': {
            'Meta': {'object_name': 'Mood'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1600', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['facts']