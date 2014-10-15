# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.conf import settings
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TouristicEventUsage'
        db.create_table('o_b_evenement_touristique_usage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usage', self.gf('django.db.models.fields.CharField')(max_length=128, db_column='usage')),
        ))
        db.send_create_signal(u'tourism', ['TouristicEventUsage'])

        # Adding model 'TouristicEventPublic'
        db.create_table('o_b_evenement_touristique_public', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('public', self.gf('django.db.models.fields.CharField')(max_length=128, db_column='public')),
        ))
        db.send_create_signal(u'tourism', ['TouristicEventPublic'])

        # Adding model 'TouristicEvent'
        db.create_table('t_t_evenement_touristique', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('structure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['authent.Structure'], db_column='structure')),
            ('date_insert', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_column='date_insert', blank=True)),
            ('date_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, db_column='date_update', blank=True)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False, db_column='supprime')),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False, db_column='public')),
            ('publication_date', self.gf('django.db.models.fields.DateField')(null=True, db_column='date_publication', blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128, db_column='nom')),
            ('description_teaser', self.gf('django.db.models.fields.TextField')(db_column='chapeau', blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(db_column='description', blank=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=settings.SRID)),
            ('begin_date', self.gf('django.db.models.fields.DateField')(null=True, db_column='date_debut', blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, db_column='date_fin', blank=True)),
            ('duration', self.gf('django.db.models.fields.CharField')(max_length=64, db_column='duree', blank=True)),
            ('meeting_point', self.gf('django.db.models.fields.CharField')(max_length=256, db_column='point_rdv', blank=True)),
            ('meeting_time', self.gf('django.db.models.fields.CharField')(max_length=64, db_column='heure_rdv', blank=True)),
            ('contact', self.gf('django.db.models.fields.TextField')(db_column='contact', blank=True)),
            ('organizer', self.gf('django.db.models.fields.CharField')(max_length=256, db_column='organisateur', blank=True)),
            ('speaker', self.gf('django.db.models.fields.CharField')(max_length=256, db_column='intervenant', blank=True)),
            ('usage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tourism.TouristicEventUsage'], null=True, db_column='usage', blank=True)),
            ('accessibility', self.gf('django.db.models.fields.CharField')(max_length=256, db_column='accessibilite', blank=True)),
            ('participant_number', self.gf('django.db.models.fields.CharField')(max_length=256, db_column='nb_places', blank=True)),
            ('booking', self.gf('django.db.models.fields.TextField')(db_column='reservation', blank=True)),
            ('public', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tourism.TouristicEventPublic'], null=True, db_column='public_vise', blank=True)),
            ('practical_info', self.gf('django.db.models.fields.TextField')(db_column='infos_pratiques', blank=True)),
        ))
        db.send_create_signal(u'tourism', ['TouristicEvent'])

        # Adding M2M table for field themes on 'TouristicEvent'
        m2m_table_name = 'o_r_evenement_touristique_theme'
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('touristicevent', models.ForeignKey(orm[u'tourism.touristicevent'], null=False)),
            ('theme', models.ForeignKey(orm[u'common.theme'], null=False))
        ))
        db.create_unique(m2m_table_name, ['touristicevent_id', 'theme_id'])


    def backwards(self, orm):
        # Deleting model 'TouristicEventUsage'
        db.delete_table('o_b_evenement_touristique_usage')

        # Deleting model 'TouristicEventPublic'
        db.delete_table('o_b_evenement_touristique_public')

        # Deleting model 'TouristicEvent'
        db.delete_table('t_t_evenement_touristique')

        # Removing M2M table for field themes on 'TouristicEvent'
        db.delete_table('o_r_evenement_touristique_theme')


    models = {
        u'authent.structure': {
            'Meta': {'ordering': "['name']", 'object_name': 'Structure'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'common.theme': {
            'Meta': {'ordering': "['label']", 'object_name': 'Theme', 'db_table': "'o_b_theme'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'theme'"}),
            'pictogram': ('django.db.models.fields.files.FileField', [], {'max_length': '512', 'null': 'True', 'db_column': "'picto'"})
        },
        u'tourism.datasource': {
            'Meta': {'ordering': "['title', 'url']", 'object_name': 'DataSource', 'db_table': "'t_t_source_donnees'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pictogram': ('django.db.models.fields.files.FileField', [], {'max_length': '512', 'db_column': "'picto'"}),
            'targets': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'titre'"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '32', 'db_column': "'type'"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '400', 'db_column': "'url'"})
        },
        u'tourism.informationdesk': {
            'Meta': {'ordering': "['name']", 'object_name': 'InformationDesk', 'db_table': "'o_b_renseignement'"},
            'description': ('django.db.models.fields.TextField', [], {'db_column': "'description'", 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '256', 'null': 'True', 'db_column': "'email'", 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': str(settings.SRID), 'null': 'True', 'spatial_index': 'False', 'db_column': "'geom'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipality': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'db_column': "'commune'", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'db_column': "'nom'"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'db_column': "'telephone'", 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '512', 'null': 'True', 'db_column': "'photo'", 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'db_column': "'code'", 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'db_column': "'rue'", 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'desks'", 'db_column': "'type'", 'to': u"orm['tourism.InformationDeskType']"}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '256', 'null': 'True', 'db_column': "'website'", 'blank': 'True'})
        },
        u'tourism.informationdesktype': {
            'Meta': {'ordering': "['label']", 'object_name': 'InformationDeskType', 'db_table': "'o_b_type_renseignement'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'label'"}),
            'pictogram': ('django.db.models.fields.files.FileField', [], {'max_length': '512', 'null': 'True', 'db_column': "'picto'"})
        },
        u'tourism.touristiccontent': {
            'Meta': {'object_name': 'TouristicContent', 'db_table': "'t_t_contenu_touristique'"},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contents'", 'db_column': "'categorie'", 'to': u"orm['tourism.TouristicContentCategory']"}),
            'date_insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_column': "'date_insert'", 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_column': "'date_update'", 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "'supprime'"}),
            'geom': ('django.contrib.gis.db.models.fields.GeometryField', [], {'srid': str(settings.SRID)}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'nom'"}),
            'publication_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'date_publication'", 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "'public'"}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['authent.Structure']", 'db_column': "'structure'"})
        },
        u'tourism.touristiccontentcategory': {
            'Meta': {'ordering': "['label']", 'object_name': 'TouristicContentCategory', 'db_table': "'t_b_contenu_touristique'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'nom'"}),
            'pictogram': ('django.db.models.fields.files.FileField', [], {'max_length': '512', 'null': 'True', 'db_column': "'picto'"})
        },
        u'tourism.touristicevent': {
            'Meta': {'ordering': "['-begin_date']", 'object_name': 'TouristicEvent', 'db_table': "'t_t_evenement_touristique'"},
            'accessibility': ('django.db.models.fields.CharField', [], {'max_length': '256', 'db_column': "'accessibilite'", 'blank': 'True'}),
            'begin_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'date_debut'", 'blank': 'True'}),
            'booking': ('django.db.models.fields.TextField', [], {'db_column': "'reservation'", 'blank': 'True'}),
            'contact': ('django.db.models.fields.TextField', [], {'db_column': "'contact'", 'blank': 'True'}),
            'date_insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_column': "'date_insert'", 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_column': "'date_update'", 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "'supprime'"}),
            'description': ('django.db.models.fields.TextField', [], {'db_column': "'description'", 'blank': 'True'}),
            'description_teaser': ('django.db.models.fields.TextField', [], {'db_column': "'chapeau'", 'blank': 'True'}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_column': "'duree'", 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'date_fin'", 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': str(settings.SRID)}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meeting_point': ('django.db.models.fields.CharField', [], {'max_length': '256', 'db_column': "'point_rdv'", 'blank': 'True'}),
            'meeting_time': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_column': "'heure_rdv'", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'nom'"}),
            'organizer': ('django.db.models.fields.CharField', [], {'max_length': '256', 'db_column': "'organisateur'", 'blank': 'True'}),
            'participant_number': ('django.db.models.fields.CharField', [], {'max_length': '256', 'db_column': "'nb_places'", 'blank': 'True'}),
            'practical_info': ('django.db.models.fields.TextField', [], {'db_column': "'infos_pratiques'", 'blank': 'True'}),
            'public': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tourism.TouristicEventPublic']", 'null': 'True', 'db_column': "'public_vise'", 'blank': 'True'}),
            'publication_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'date_publication'", 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "'public'"}),
            'speaker': ('django.db.models.fields.CharField', [], {'max_length': '256', 'db_column': "'intervenant'", 'blank': 'True'}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['authent.Structure']", 'db_column': "'structure'"}),
            'themes': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'events'", 'to': u"orm['common.Theme']", 'db_table': "'o_r_evenement_touristique_theme'", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'usage': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tourism.TouristicEventUsage']", 'null': 'True', 'db_column': "'usage'", 'blank': 'True'})
        },
        u'tourism.touristiceventpublic': {
            'Meta': {'ordering': "['public']", 'object_name': 'TouristicEventPublic', 'db_table': "'o_b_evenement_touristique_public'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'public'"})
        },
        u'tourism.touristiceventusage': {
            'Meta': {'ordering': "['usage']", 'object_name': 'TouristicEventUsage', 'db_table': "'o_b_evenement_touristique_usage'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'usage': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'usage'"})
        }
    }

    complete_apps = ['tourism']