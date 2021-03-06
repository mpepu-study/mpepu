# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Processing'
#         db.create_table(u'mpepu_lab_processing', (
#             ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
#             ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
#             ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
#             ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
#             ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, db_index=True, blank=True)),
#             ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, db_index=True, blank=True)),
#             ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
#             ('revision', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
#             ('print_labels', self.gf('django.db.models.fields.BooleanField')(default=True)),
#             ('aliquot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_lab.Aliquot'])),
#             ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_lab.Profile'])),
#         ))
#         db.send_create_signal('mpepu_lab', ['Processing'])

        # Adding model 'AliquotType'
#         db.create_table(u'mpepu_lab_aliquottype', (
#             (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
#             ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
#             ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
#             ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
#             ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
#             ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, db_index=True, blank=True)),
#             ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, db_index=True, blank=True)),
#             ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
#             ('alpha_code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=15)),
#             ('numeric_code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2)),
#         ))
#         db.send_create_signal('mpepu_lab', ['AliquotType'])

        # Adding model 'AliquotCondition'
#         db.create_table(u'mpepu_lab_aliquotcondition', (
#             (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
#             ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
#             ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
#             ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
#             ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
#             ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, db_index=True, blank=True)),
#             ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, db_index=True, blank=True)),
#             ('name', self.gf('django.db.models.fields.CharField')(max_length=250, unique=True, null=True, db_index=True)),
#             ('short_name', self.gf('django.db.models.fields.CharField')(max_length=250, unique=True, null=True, db_index=True)),
#             ('display_index', self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True)),
#             ('field_name', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
#             ('version', self.gf('django.db.models.fields.CharField')(default='1.0', max_length=35)),
#         ))
#         db.send_create_signal('mpepu_lab', ['AliquotCondition'])

        # Adding model 'Aliquot'
#         db.create_table(u'mpepu_lab_aliquot', (
#             ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
#             ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
#             ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
#             ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
#             ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, db_index=True, blank=True)),
#             ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, db_index=True, blank=True)),
#             ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
#             ('revision', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
#             ('primary_aliquot', self.gf('django.db.models.fields.related.ForeignKey')(related_name='primary', null=True, to=orm['mpepu_lab.Aliquot'])),
#             ('source_aliquot', self.gf('django.db.models.fields.related.ForeignKey')(related_name='source', null=True, to=orm['mpepu_lab.Aliquot'])),
#             ('aliquot_identifier', self.gf('django.db.models.fields.CharField')(unique=True, max_length=25)),
#             ('aliquot_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 4, 0, 0))),
#             ('count', self.gf('django.db.models.fields.IntegerField')(null=True)),
#             ('medium', self.gf('django.db.models.fields.CharField')(default='TUBE', max_length=25)),
#             ('original_measure', self.gf('django.db.models.fields.DecimalField')(default='5.00', max_digits=10, decimal_places=2)),
#             ('current_measure', self.gf('django.db.models.fields.DecimalField')(default='5.00', max_digits=10, decimal_places=2)),
#             ('measure_units', self.gf('django.db.models.fields.CharField')(default='mL', max_length=25)),
#             ('status', self.gf('django.db.models.fields.CharField')(default='available', max_length=25)),
#             ('comment', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
#             ('subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
#             ('is_packed', self.gf('django.db.models.fields.BooleanField')(default=False)),
#             ('receive_identifier', self.gf('django.db.models.fields.CharField')(max_length=25, null=True)),
#             ('receive', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_lab.Receive'])),
#             ('aliquot_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_lab.AliquotType'], null=True)),
#             ('aliquot_condition', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_lab.AliquotCondition'], null=True, blank=True)),
#         ))
#         db.send_create_signal('mpepu_lab', ['Aliquot'])

        # Adding unique constraint on 'Aliquot', fields ['receive', 'count']
        #db.create_unique(u'mpepu_lab_aliquot', ['receive_id', 'count'])

        # Adding model 'Profile'
#         db.create_table(u'mpepu_lab_profile', (
#             ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
#             ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
#             ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
#             ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
#             ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, db_index=True, blank=True)),
#             ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, db_index=True, blank=True)),
#             ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
#             ('revision', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
#             ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
#             ('aliquot_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_lab.AliquotType'])),
#         ))
#         db.send_create_signal('mpepu_lab', ['Profile'])

        # Adding model 'Receive'
#         db.create_table(u'mpepu_lab_receive', (
#             ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
#             ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
#             ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
#             ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
#             ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, db_index=True, blank=True)),
#             ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, db_index=True, blank=True)),
#             ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
#             ('revision', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
#             ('receive_identifier', self.gf('django.db.models.fields.CharField')(max_length=25, unique=True, null=True, db_index=True)),
#             ('requisition_identifier', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=25, null=True, blank=True)),
#             ('drawn_datetime', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
#             ('receive_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 4, 0, 0), db_index=True)),
#             ('visit', self.gf('django.db.models.fields.CharField')(max_length=25)),
#             ('clinician_initials', self.gf('django.db.models.fields.CharField')(max_length=3)),
#             ('receive_condition', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
#             ('import_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True)),
#             ('registered_subject', self.gf('django.db.models.fields.related.ForeignKey')(related_name='mpepu_receive', null=True, to=orm['registration.RegisteredSubject'])),
#             ('requisition_model_name', self.gf('django.db.models.fields.CharField')(max_length=25, null=True)),
#             ('subject_type', self.gf('django.db.models.fields.CharField')(max_length=25, null=True)),
#         ))
#         db.send_create_signal('mpepu_lab', ['Receive'])

        # Adding model 'ProfileItem'
#         db.create_table(u'mpepu_lab_profileitem', (
#             ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
#             ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
#             ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
#             ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
#             ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, db_index=True, blank=True)),
#             ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, db_index=True, blank=True)),
#             ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
#             ('revision', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
#             ('volume', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=1)),
#             ('count', self.gf('django.db.models.fields.IntegerField')()),
#             ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_lab.Profile'])),
#             ('aliquot_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_lab.AliquotType'])),
#         ))
#         db.send_create_signal('mpepu_lab', ['ProfileItem'])

        # Adding model 'Panel'
#         db.create_table(u'mpepu_lab_panel', (
#             (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
#             ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
#             ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
#             ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
#             ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
#             ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, db_index=True, blank=True)),
#             ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, db_index=True, blank=True)),
#             ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50, db_index=True)),
#             ('comment', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
#             ('panel_type', self.gf('django.db.models.fields.CharField')(default='TEST', max_length=15)),
#         ))
#         db.send_create_signal('mpepu_lab', ['Panel'])

        # Adding M2M table for field test_code on 'Panel'
#         m2m_table_name = db.shorten_name(u'mpepu_lab_panel_test_code')
#         db.create_table(m2m_table_name, (
#             ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
#             ('panel', models.ForeignKey(orm['mpepu_lab.panel'], null=False)),
#             ('testcode', models.ForeignKey(orm['lab_clinic_api.testcode'], null=False))
#         ))
#         db.create_unique(m2m_table_name, ['panel_id', 'testcode_id'])

        # Adding M2M table for field aliquot_type on 'Panel'
#         m2m_table_name = db.shorten_name(u'mpepu_lab_panel_aliquot_type')
#         db.create_table(m2m_table_name, (
#             ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
#             ('panel', models.ForeignKey(orm['mpepu_lab.panel'], null=False)),
#             ('aliquottype', models.ForeignKey(orm['mpepu_lab.aliquottype'], null=False))
#         ))
#         db.create_unique(m2m_table_name, ['panel_id', 'aliquottype_id'])

        # Adding field 'InfantRequisitionAudit.revision'
#         db.add_column(u'mpepu_lab_infantrequisition_audit', 'revision',
#                       self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
#                       keep_default=False)
# 
#         # Adding field 'InfantRequisitionAudit.subject_identifier'
#         db.add_column(u'mpepu_lab_infantrequisition_audit', 'subject_identifier',
#                       self.gf('django.db.models.fields.CharField')(max_length=25, null=True),
#                       keep_default=False)
# 
#         # Adding field 'InfantRequisitionAudit.packing_list'
#         db.add_column(u'mpepu_lab_infantrequisition_audit', 'packing_list',
#                       self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='_audit_infantrequisition', null=True, to=orm['mpepu_lab.PackingList']),
#                       keep_default=False)
# 
# 
#         # Changing field 'InfantRequisitionAudit.specimen_identifier'
#         db.alter_column(u'mpepu_lab_infantrequisition_audit', 'specimen_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))
# 
#         # Changing field 'InfantRequisitionAudit.aliquot_type'
#         db.alter_column(u'mpepu_lab_infantrequisition_audit', 'aliquot_type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_lab.AliquotType']))
# 
#         # Changing field 'InfantRequisitionAudit.site'
#         db.alter_column(u'mpepu_lab_infantrequisition_audit', 'site_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['bhp_variables.StudySite']))
# 
#         # Changing field 'InfantRequisitionAudit.requisition_identifier'
#         db.alter_column(u'mpepu_lab_infantrequisition_audit', 'requisition_identifier', self.gf('django.db.models.fields.CharField')(max_length=50))
# 
#         # Changing field 'InfantRequisitionAudit.panel'
#         db.alter_column(u'mpepu_lab_infantrequisition_audit', 'panel_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_lab.Panel']))
# 
#         # Changing field 'InfantRequisitionAudit.estimated_volume'
#         db.alter_column(u'mpepu_lab_infantrequisition_audit', 'estimated_volume', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2))
#         # Adding field 'MaternalRequisitionAudit.revision'
#         db.add_column(u'mpepu_lab_maternalrequisition_audit', 'revision',
#                       self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
#                       keep_default=False)

        # Adding field 'MaternalRequisitionAudit.subject_identifier'
#         db.add_column(u'mpepu_lab_maternalrequisition_audit', 'subject_identifier',
#                       self.gf('django.db.models.fields.CharField')(max_length=25, null=True),
#                       keep_default=False)
# 
#         # Adding field 'MaternalRequisitionAudit.packing_list'
#         db.add_column(u'mpepu_lab_maternalrequisition_audit', 'packing_list',
#                       self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='_audit_maternalrequisition', null=True, to=orm['mpepu_lab.PackingList']),
#                       keep_default=False)


        # Changing field 'MaternalRequisitionAudit.specimen_identifier'
#         db.alter_column(u'mpepu_lab_maternalrequisition_audit', 'specimen_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'MaternalRequisitionAudit.aliquot_type'
#         db.alter_column(u'mpepu_lab_maternalrequisition_audit', 'aliquot_type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_lab.AliquotType']))

        # Changing field 'MaternalRequisitionAudit.site'
#         db.alter_column(u'mpepu_lab_maternalrequisition_audit', 'site_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['bhp_variables.StudySite']))
# 
#         # Changing field 'MaternalRequisitionAudit.requisition_identifier'
#         db.alter_column(u'mpepu_lab_maternalrequisition_audit', 'requisition_identifier', self.gf('django.db.models.fields.CharField')(max_length=50))
# 
#         # Changing field 'MaternalRequisitionAudit.panel'
#         db.alter_column(u'mpepu_lab_maternalrequisition_audit', 'panel_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_lab.Panel']))
# 
#         # Changing field 'MaternalRequisitionAudit.estimated_volume'
#         db.alter_column(u'mpepu_lab_maternalrequisition_audit', 'estimated_volume', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2))
        # Adding field 'InfantRequisition.revision'
#         db.add_column(u'mpepu_lab_infantrequisition', 'revision',
#                       self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
#                       keep_default=False)
# 
#         # Adding field 'InfantRequisition.subject_identifier'
#         db.add_column(u'mpepu_lab_infantrequisition', 'subject_identifier',
#                       self.gf('django.db.models.fields.CharField')(max_length=25, null=True),
#                       keep_default=False)
# 
#         # Adding field 'InfantRequisition.packing_list'
#         db.add_column(u'mpepu_lab_infantrequisition', 'packing_list',
#                       self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_lab.PackingList'], null=True, blank=True),
#                       keep_default=False)


        # Changing field 'InfantRequisition.specimen_identifier'
#         db.alter_column(u'mpepu_lab_infantrequisition', 'specimen_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, unique=True, null=True))
# 
#         # Changing field 'InfantRequisition.site'
#         db.alter_column(u'mpepu_lab_infantrequisition', 'site_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_variables.StudySite'], null=True))
# 
#         # Changing field 'InfantRequisition.requisition_identifier'
#         db.alter_column(u'mpepu_lab_infantrequisition', 'requisition_identifier', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50))
# 
#         # Changing field 'InfantRequisition.panel'
#         db.alter_column(u'mpepu_lab_infantrequisition', 'panel_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_lab.Panel']))
# 
#         # Changing field 'InfantRequisition.aliquot_type'
#         db.alter_column(u'mpepu_lab_infantrequisition', 'aliquot_type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_lab.AliquotType']))
# 
#         # Changing field 'InfantRequisition.estimated_volume'
#         db.alter_column(u'mpepu_lab_infantrequisition', 'estimated_volume', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2))
#         # Adding unique constraint on 'InfantRequisition', fields ['infant_visit', 'panel', 'is_drawn']
#         db.create_unique(u'mpepu_lab_infantrequisition', ['infant_visit_id', 'panel_id', 'is_drawn'])

        # Adding field 'MaternalRequisition.revision'
        db.add_column(u'mpepu_lab_maternalrequisition', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalRequisition.subject_identifier'
        db.add_column(u'mpepu_lab_maternalrequisition', 'subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=25, null=True),
                      keep_default=False)

        # Adding field 'MaternalRequisition.packing_list'
        db.add_column(u'mpepu_lab_maternalrequisition', 'packing_list',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_lab.PackingList'], null=True, blank=True),
                      keep_default=False)


        # Changing field 'MaternalRequisition.specimen_identifier'
        db.alter_column(u'mpepu_lab_maternalrequisition', 'specimen_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, unique=True, null=True))

        # Changing field 'MaternalRequisition.site'
        db.alter_column(u'mpepu_lab_maternalrequisition', 'site_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_variables.StudySite'], null=True))

        # Changing field 'MaternalRequisition.requisition_identifier'
        db.alter_column(u'mpepu_lab_maternalrequisition', 'requisition_identifier', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50))

        # Changing field 'MaternalRequisition.panel'
        db.alter_column(u'mpepu_lab_maternalrequisition', 'panel_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_lab.Panel']))

        # Changing field 'MaternalRequisition.aliquot_type'
        db.alter_column(u'mpepu_lab_maternalrequisition', 'aliquot_type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_lab.AliquotType']))

        # Changing field 'MaternalRequisition.estimated_volume'
        db.alter_column(u'mpepu_lab_maternalrequisition', 'estimated_volume', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2))
        # Adding unique constraint on 'MaternalRequisition', fields ['maternal_visit', 'panel', 'is_drawn']
#         db.create_unique(u'mpepu_lab_maternalrequisition', ['maternal_visit_id', 'panel_id', 'is_drawn'])

        # Adding field 'PackingList.revision'
        db.add_column(u'mpepu_lab_packinglist', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'PackingListItem.revision'
        db.add_column(u'mpepu_lab_packinglistitem', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)


        # Changing field 'PackingListItem.packing_list'
        db.alter_column(u'mpepu_lab_packinglistitem', 'packing_list_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_lab.PackingList'], null=True))

        # Changing field 'PackingListItem.requisition'
        db.alter_column(u'mpepu_lab_packinglistitem', 'requisition', self.gf('django.db.models.fields.CharField')(max_length=36, null=True))

    def backwards(self, orm):
        pass
        # Removing unique constraint on 'MaternalRequisition', fields ['maternal_visit', 'panel', 'is_drawn']
#         db.delete_unique(u'mpepu_lab_maternalrequisition', ['maternal_visit_id', 'panel_id', 'is_drawn'])
# 
#         # Removing unique constraint on 'InfantRequisition', fields ['infant_visit', 'panel', 'is_drawn']
#         db.delete_unique(u'mpepu_lab_infantrequisition', ['infant_visit_id', 'panel_id', 'is_drawn'])
# 
#         # Removing unique constraint on 'Aliquot', fields ['receive', 'count']
#         db.delete_unique(u'mpepu_lab_aliquot', ['receive_id', 'count'])
# 
#         # Deleting model 'Processing'
#         db.delete_table(u'mpepu_lab_processing')
# 
#         # Deleting model 'AliquotType'
#         db.delete_table(u'mpepu_lab_aliquottype')
# 
#         # Deleting model 'AliquotCondition'
#         db.delete_table(u'mpepu_lab_aliquotcondition')
# 
#         # Deleting model 'Aliquot'
#         db.delete_table(u'mpepu_lab_aliquot')
# 
#         # Deleting model 'Profile'
#         db.delete_table(u'mpepu_lab_profile')
# 
#         # Deleting model 'Receive'
#         db.delete_table(u'mpepu_lab_receive')
# 
#         # Deleting model 'ProfileItem'
#         db.delete_table(u'mpepu_lab_profileitem')
# 
#         # Deleting model 'Panel'
#         db.delete_table(u'mpepu_lab_panel')
# 
#         # Removing M2M table for field test_code on 'Panel'
#         db.delete_table(db.shorten_name(u'mpepu_lab_panel_test_code'))
# 
#         # Removing M2M table for field aliquot_type on 'Panel'
#         db.delete_table(db.shorten_name(u'mpepu_lab_panel_aliquot_type'))
# 
#         # Deleting field 'InfantRequisitionAudit.revision'
#         db.delete_column(u'mpepu_lab_infantrequisition_audit', 'revision')
# 
#         # Deleting field 'InfantRequisitionAudit.subject_identifier'
#         db.delete_column(u'mpepu_lab_infantrequisition_audit', 'subject_identifier')
# 
#         # Deleting field 'InfantRequisitionAudit.packing_list'
#         db.delete_column(u'mpepu_lab_infantrequisition_audit', 'packing_list_id')
# 
# 
#         # Changing field 'InfantRequisitionAudit.specimen_identifier'
#         db.alter_column(u'mpepu_lab_infantrequisition_audit', 'specimen_identifier', self.gf('django.db.models.fields.CharField')(max_length=25, null=True))
# 
#         # Changing field 'InfantRequisitionAudit.aliquot_type'
#         db.alter_column(u'mpepu_lab_infantrequisition_audit', 'aliquot_type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_clinic_api.AliquotType']))
# 
#         # Changing field 'InfantRequisitionAudit.site'
#         db.alter_column(u'mpepu_lab_infantrequisition_audit', 'site_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['bhp_variables.StudySite']))
# 
#         # Changing field 'InfantRequisitionAudit.requisition_identifier'
#         db.alter_column(u'mpepu_lab_infantrequisition_audit', 'requisition_identifier', self.gf('django.db.models.fields.CharField')(max_length=25))
# 
#         # Changing field 'InfantRequisitionAudit.panel'
#         db.alter_column(u'mpepu_lab_infantrequisition_audit', 'panel_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_clinic_api.Panel']))
# 
#         # Changing field 'InfantRequisitionAudit.estimated_volume'
#         db.alter_column(u'mpepu_lab_infantrequisition_audit', 'estimated_volume', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=1))
#         # Deleting field 'MaternalRequisitionAudit.revision'
#         db.delete_column(u'mpepu_lab_maternalrequisition_audit', 'revision')
# 
#         # Deleting field 'MaternalRequisitionAudit.subject_identifier'
#         db.delete_column(u'mpepu_lab_maternalrequisition_audit', 'subject_identifier')
# 
#         # Deleting field 'MaternalRequisitionAudit.packing_list'
#         db.delete_column(u'mpepu_lab_maternalrequisition_audit', 'packing_list_id')
# 
# 
#         # Changing field 'MaternalRequisitionAudit.specimen_identifier'
#         db.alter_column(u'mpepu_lab_maternalrequisition_audit', 'specimen_identifier', self.gf('django.db.models.fields.CharField')(max_length=25, null=True))
# 
#         # Changing field 'MaternalRequisitionAudit.aliquot_type'
#         db.alter_column(u'mpepu_lab_maternalrequisition_audit', 'aliquot_type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_clinic_api.AliquotType']))
# 
#         # Changing field 'MaternalRequisitionAudit.site'
#         db.alter_column(u'mpepu_lab_maternalrequisition_audit', 'site_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['bhp_variables.StudySite']))
# 
#         # Changing field 'MaternalRequisitionAudit.requisition_identifier'
#         db.alter_column(u'mpepu_lab_maternalrequisition_audit', 'requisition_identifier', self.gf('django.db.models.fields.CharField')(max_length=25))
# 
#         # Changing field 'MaternalRequisitionAudit.panel'
#         db.alter_column(u'mpepu_lab_maternalrequisition_audit', 'panel_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_clinic_api.Panel']))
# 
#         # Changing field 'MaternalRequisitionAudit.estimated_volume'
#         db.alter_column(u'mpepu_lab_maternalrequisition_audit', 'estimated_volume', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=1))
#         # Deleting field 'InfantRequisition.revision'
#         db.delete_column(u'mpepu_lab_infantrequisition', 'revision')
# 
#         # Deleting field 'InfantRequisition.subject_identifier'
#         db.delete_column(u'mpepu_lab_infantrequisition', 'subject_identifier')
# 
#         # Deleting field 'InfantRequisition.packing_list'
#         db.delete_column(u'mpepu_lab_infantrequisition', 'packing_list_id')
# 
# 
#         # Changing field 'InfantRequisition.specimen_identifier'
#         db.alter_column(u'mpepu_lab_infantrequisition', 'specimen_identifier', self.gf('django.db.models.fields.CharField')(unique=True, max_length=25, null=True))
# 
#         # Changing field 'InfantRequisition.site'
#         db.alter_column(u'mpepu_lab_infantrequisition', 'site_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['bhp_variables.StudySite']))
# 
#         # Changing field 'InfantRequisition.requisition_identifier'
#         db.alter_column(u'mpepu_lab_infantrequisition', 'requisition_identifier', self.gf('django.db.models.fields.CharField')(max_length=25, unique=True))
# 
#         # Changing field 'InfantRequisition.panel'
#         db.alter_column(u'mpepu_lab_infantrequisition', 'panel_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_clinic_api.Panel']))
# 
#         # Changing field 'InfantRequisition.aliquot_type'
#         db.alter_column(u'mpepu_lab_infantrequisition', 'aliquot_type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_clinic_api.AliquotType']))
# 
#         # Changing field 'InfantRequisition.estimated_volume'
#         db.alter_column(u'mpepu_lab_infantrequisition', 'estimated_volume', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=1))
#         # Deleting field 'MaternalRequisition.revision'
#         db.delete_column(u'mpepu_lab_maternalrequisition', 'revision')
# 
#         # Deleting field 'MaternalRequisition.subject_identifier'
#         db.delete_column(u'mpepu_lab_maternalrequisition', 'subject_identifier')
# 
#         # Deleting field 'MaternalRequisition.packing_list'
#         db.delete_column(u'mpepu_lab_maternalrequisition', 'packing_list_id')
# 
# 
#         # Changing field 'MaternalRequisition.specimen_identifier'
#         db.alter_column(u'mpepu_lab_maternalrequisition', 'specimen_identifier', self.gf('django.db.models.fields.CharField')(unique=True, max_length=25, null=True))
# 
#         # Changing field 'MaternalRequisition.site'
#         db.alter_column(u'mpepu_lab_maternalrequisition', 'site_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['bhp_variables.StudySite']))
# 
#         # Changing field 'MaternalRequisition.requisition_identifier'
#         db.alter_column(u'mpepu_lab_maternalrequisition', 'requisition_identifier', self.gf('django.db.models.fields.CharField')(max_length=25, unique=True))
# 
#         # Changing field 'MaternalRequisition.panel'
#         db.alter_column(u'mpepu_lab_maternalrequisition', 'panel_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_clinic_api.Panel']))
# 
#         # Changing field 'MaternalRequisition.aliquot_type'
#         db.alter_column(u'mpepu_lab_maternalrequisition', 'aliquot_type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_clinic_api.AliquotType']))
# 
#         # Changing field 'MaternalRequisition.estimated_volume'
#         db.alter_column(u'mpepu_lab_maternalrequisition', 'estimated_volume', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=1))
#         # Deleting field 'PackingList.revision'
#         db.delete_column(u'mpepu_lab_packinglist', 'revision')
# 
#         # Deleting field 'PackingListItem.revision'
#         db.delete_column(u'mpepu_lab_packinglistitem', 'revision')
# 
# 
#         # Changing field 'PackingListItem.packing_list'
#         db.alter_column(u'mpepu_lab_packinglistitem', 'packing_list_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['mpepu_lab.PackingList']))
# 
#         # Changing field 'PackingListItem.requisition'
#         db.alter_column(u'mpepu_lab_packinglistitem', 'requisition', self.gf('django.db.models.fields.CharField')(max_length=35, null=True))

    models = {
        'appointment.appointment': {
            'Meta': {'ordering': "['registered_subject', 'appt_datetime']", 'unique_together': "(('registered_subject', 'visit_definition', 'visit_instance'),)", 'object_name': 'Appointment', 'db_table': "'bhp_appointment_appointment'"},
            'appt_close_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'appt_datetime': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'appt_reason': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'appt_status': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '25', 'db_index': 'True'}),
            'appt_type': ('django.db.models.fields.CharField', [], {'default': "'clinic'", 'max_length': '20'}),
            'best_appt_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'contact_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'contact_tel': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dashboard_type': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'is_confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['registration.RegisteredSubject']"}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'study_site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_variables.StudySite']", 'null': 'True'}),
            'timepoint_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'visit_definition': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['visit_schedule.VisitDefinition']"}),
            'visit_instance': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1', 'null': 'True', 'db_index': 'True', 'blank': 'True'})
        },
        'bhp_content_type_map.contenttypemap': {
            'Meta': {'ordering': "['name']", 'unique_together': "(['app_label', 'model'],)", 'object_name': 'ContentTypeMap'},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'module_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'bhp_variables.studysite': {
            'Meta': {'ordering': "['site_code']", 'unique_together': "[('site_code', 'site_name')]", 'object_name': 'StudySite'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'site_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4'}),
            'site_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'lab_clinic_api.aliquottype': {
            'Meta': {'ordering': "['name']", 'object_name': 'AliquotType'},
            'alpha_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'numeric_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'lab_clinic_api.panel': {
            'Meta': {'object_name': 'Panel'},
            'aliquot_type': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lab_clinic_api.AliquotType']", 'symmetrical': 'False'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'edc_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'panel_type': ('django.db.models.fields.CharField', [], {'default': "'TEST'", 'max_length': '15'}),
            'test_code': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['lab_clinic_api.TestCode']", 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'lab_clinic_api.testcode': {
            'Meta': {'ordering': "['edc_name']", 'object_name': 'TestCode'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_decimal_places': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'edc_code': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'db_index': 'True'}),
            'edc_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'db_index': 'True'}),
            'formula': ('django.db.models.fields.CharField', [], {'max_length': "'50'", 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_absolute': ('django.db.models.fields.CharField', [], {'default': "'absolute'", 'max_length': "'15'"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'test_code_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lab_clinic_api.TestCodeGroup']", 'null': 'True'}),
            'units': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'lab_clinic_api.testcodegroup': {
            'Meta': {'ordering': "['code']", 'object_name': 'TestCodeGroup'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantvisit': {
            'Meta': {'object_name': 'InfantVisit'},
            'appointment': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['appointment.Appointment']", 'unique': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_last_alive': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'info_source': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'info_source_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'information_provider': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'information_provider_other': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'reason_missed': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'study_status': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'survival_status': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_lab.aliquot': {
            'Meta': {'ordering': "('receive', 'count')", 'unique_together': "(('receive', 'count'),)", 'object_name': 'Aliquot'},
            'aliquot_condition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_lab.AliquotCondition']", 'null': 'True', 'blank': 'True'}),
            'aliquot_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 4, 0, 0)'}),
            'aliquot_identifier': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'}),
            'aliquot_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_lab.AliquotType']", 'null': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'count': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'current_measure': ('django.db.models.fields.DecimalField', [], {'default': "'5.00'", 'max_digits': '10', 'decimal_places': '2'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'is_packed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'measure_units': ('django.db.models.fields.CharField', [], {'default': "'mL'", 'max_length': '25'}),
            'medium': ('django.db.models.fields.CharField', [], {'default': "'TUBE'", 'max_length': '25'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'original_measure': ('django.db.models.fields.DecimalField', [], {'default': "'5.00'", 'max_digits': '10', 'decimal_places': '2'}),
            'primary_aliquot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'primary'", 'null': 'True', 'to': "orm['mpepu_lab.Aliquot']"}),
            'receive': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_lab.Receive']"}),
            'receive_identifier': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'source_aliquot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'source'", 'null': 'True', 'to': "orm['mpepu_lab.Aliquot']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'available'", 'max_length': '25'}),
            'subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_lab.aliquotcondition': {
            'Meta': {'object_name': 'AliquotCondition'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_lab.aliquottype': {
            'Meta': {'ordering': "['name']", 'object_name': 'AliquotType'},
            'alpha_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'numeric_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_lab.infantrequisition': {
            'Meta': {'unique_together': "(('infant_visit', 'panel', 'is_drawn'),)", 'object_name': 'InfantRequisition'},
            'aliquot_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_lab.AliquotType']"}),
            'clinician_initials': ('django.db.models.fields.CharField', [], {'default': "'--'", 'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dmis_identifier': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'drawn_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'estimated_volume': ('django.db.models.fields.DecimalField', [], {'default': '5.0', 'max_digits': '7', 'decimal_places': '2'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'is_drawn': ('django.db.models.fields.CharField', [], {'default': "'Yes'", 'max_length': '3'}),
            'is_labelled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_labelled_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'is_lis': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_packed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_receive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_receive_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'item_count_total': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'item_type': ('django.db.models.fields.CharField', [], {'default': "'tube'", 'max_length': '25'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'old_aliquot_type_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'old_panel_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'packing_list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_lab.PackingList']", 'null': 'True', 'blank': 'True'}),
            'panel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_lab.Panel']"}),
            'priority': ('django.db.models.fields.CharField', [], {'default': "'normal'", 'max_length': '25'}),
            'protocol': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'reason_not_drawn': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'requisition_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'requisition_identifier': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_variables.StudySite']", 'null': 'True'}),
            'specimen_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'test_code': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['lab_clinic_api.TestCode']", 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_lab.infantrequisitionaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantRequisitionAudit', 'db_table': "u'mpepu_lab_infantrequisition_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'aliquot_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantrequisition'", 'to': "orm['mpepu_lab.AliquotType']"}),
            'clinician_initials': ('django.db.models.fields.CharField', [], {'default': "'--'", 'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dmis_identifier': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'drawn_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'estimated_volume': ('django.db.models.fields.DecimalField', [], {'default': '5.0', 'max_digits': '7', 'decimal_places': '2'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantrequisition'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'is_drawn': ('django.db.models.fields.CharField', [], {'default': "'Yes'", 'max_length': '3'}),
            'is_labelled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_labelled_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'is_lis': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_packed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_receive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_receive_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'item_count_total': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'item_type': ('django.db.models.fields.CharField', [], {'default': "'tube'", 'max_length': '25'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'old_aliquot_type_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'old_panel_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'packing_list': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'_audit_infantrequisition'", 'null': 'True', 'to': "orm['mpepu_lab.PackingList']"}),
            'panel': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantrequisition'", 'to': "orm['mpepu_lab.Panel']"}),
            'priority': ('django.db.models.fields.CharField', [], {'default': "'normal'", 'max_length': '25'}),
            'protocol': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'reason_not_drawn': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'requisition_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'requisition_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantrequisition'", 'null': 'True', 'to': "orm['bhp_variables.StudySite']"}),
            'specimen_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_lab.maternalrequisition': {
            'Meta': {'unique_together': "(('maternal_visit', 'panel', 'is_drawn'),)", 'object_name': 'MaternalRequisition'},
            'aliquot_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_lab.AliquotType']"}),
            'clinician_initials': ('django.db.models.fields.CharField', [], {'default': "'--'", 'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dmis_identifier': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'drawn_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'estimated_volume': ('django.db.models.fields.DecimalField', [], {'default': '5.0', 'max_digits': '7', 'decimal_places': '2'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'is_drawn': ('django.db.models.fields.CharField', [], {'default': "'Yes'", 'max_length': '3'}),
            'is_labelled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_labelled_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'is_lis': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_packed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_receive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_receive_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'item_count_total': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'item_type': ('django.db.models.fields.CharField', [], {'default': "'tube'", 'max_length': '25'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'old_aliquot_type_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'old_panel_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'packing_list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_lab.PackingList']", 'null': 'True', 'blank': 'True'}),
            'panel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_lab.Panel']"}),
            'priority': ('django.db.models.fields.CharField', [], {'default': "'normal'", 'max_length': '25'}),
            'protocol': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'reason_not_drawn': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'requisition_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'requisition_identifier': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_variables.StudySite']", 'null': 'True'}),
            'specimen_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'test_code': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['lab_clinic_api.TestCode']", 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_lab.maternalrequisitionaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalRequisitionAudit', 'db_table': "u'mpepu_lab_maternalrequisition_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'aliquot_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalrequisition'", 'to': "orm['mpepu_lab.AliquotType']"}),
            'clinician_initials': ('django.db.models.fields.CharField', [], {'default': "'--'", 'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dmis_identifier': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'drawn_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'estimated_volume': ('django.db.models.fields.DecimalField', [], {'default': '5.0', 'max_digits': '7', 'decimal_places': '2'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'is_drawn': ('django.db.models.fields.CharField', [], {'default': "'Yes'", 'max_length': '3'}),
            'is_labelled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_labelled_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'is_lis': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_packed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_receive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_receive_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'item_count_total': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'item_type': ('django.db.models.fields.CharField', [], {'default': "'tube'", 'max_length': '25'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalrequisition'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'old_aliquot_type_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'old_panel_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'packing_list': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'_audit_maternalrequisition'", 'null': 'True', 'to': "orm['mpepu_lab.PackingList']"}),
            'panel': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalrequisition'", 'to': "orm['mpepu_lab.Panel']"}),
            'priority': ('django.db.models.fields.CharField', [], {'default': "'normal'", 'max_length': '25'}),
            'protocol': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'reason_not_drawn': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'requisition_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'requisition_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalrequisition'", 'null': 'True', 'to': "orm['bhp_variables.StudySite']"}),
            'specimen_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_lab.packinglist': {
            'Meta': {'object_name': 'PackingList'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'list_comment': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'list_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 4, 0, 0)'}),
            'list_items': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_lab.packinglistitem': {
            'Meta': {'object_name': 'PackingListItem'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'item_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'item_description': ('django.db.models.fields.TextField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'item_priority': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True'}),
            'item_reference': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'old_panel_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'packing_list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_lab.PackingList']", 'null': 'True'}),
            'panel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lab_clinic_api.Panel']", 'null': 'True', 'blank': 'True'}),
            'requisition': ('django.db.models.fields.CharField', [], {'max_length': '36', 'null': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_lab.panel': {
            'Meta': {'object_name': 'Panel'},
            'aliquot_type': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mpepu_lab.AliquotType']", 'symmetrical': 'False'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'panel_type': ('django.db.models.fields.CharField', [], {'default': "'TEST'", 'max_length': '15'}),
            'test_code': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lab_clinic_api.TestCode']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_lab.processing': {
            'Meta': {'object_name': 'Processing'},
            'aliquot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_lab.Aliquot']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'print_labels': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_lab.Profile']"}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_lab.profile': {
            'Meta': {'object_name': 'Profile'},
            'aliquot_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_lab.AliquotType']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_lab.profileitem': {
            'Meta': {'object_name': 'ProfileItem'},
            'aliquot_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_lab.AliquotType']"}),
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_lab.Profile']"}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'volume': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '1'})
        },
        'mpepu_lab.receive': {
            'Meta': {'object_name': 'Receive'},
            'clinician_initials': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'drawn_datetime': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'import_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'receive_condition': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'receive_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 4, 0, 0)', 'db_index': 'True'}),
            'receive_identifier': ('django.db.models.fields.CharField', [], {'max_length': '25', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mpepu_receive'", 'null': 'True', 'to': "orm['registration.RegisteredSubject']"}),
            'requisition_identifier': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'requisition_model_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'subject_type': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'visit': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'mpepu_maternal.maternalvisit': {
            'Meta': {'object_name': 'MaternalVisit'},
            'appointment': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['appointment.Appointment']", 'unique': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_last_alive': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'info_source': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'info_source_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'reason_missed': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'survival_status': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'registration.registeredsubject': {
            'Meta': {'ordering': "['subject_identifier']", 'unique_together': "(('first_name', 'dob', 'initials'),)", 'object_name': 'RegisteredSubject', 'db_table': "'bhp_registration_registeredsubject'"},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'hiv_status': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'identity': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'identity_type': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'is_dob_estimated': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'may_store_samples': ('django.db.models.fields.CharField', [], {'default': "'?'", 'max_length': '3'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'randomization_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'registration_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'registration_identifier': ('django.db.models.fields.CharField', [], {'max_length': '36', 'null': 'True', 'blank': 'True'}),
            'registration_status': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'relative_identifier': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'salt': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'screening_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sid': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'study_site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_variables.StudySite']", 'null': 'True', 'blank': 'True'}),
            'subject_consent_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'subject_identifier': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '50', 'blank': 'True'}),
            'subject_identifier_as_pk': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'db_index': 'True'}),
            'subject_type': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'survival_status': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'visit_schedule.membershipform': {
            'Meta': {'object_name': 'MembershipForm', 'db_table': "'bhp_visit_membershipform'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'default': "'subject'", 'max_length': '35', 'unique': 'True', 'null': 'True'}),
            'content_type_map': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'+'", 'unique': 'True', 'to': "orm['bhp_content_type_map.ContentTypeMap']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'model_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'visit_schedule.schedulegroup': {
            'Meta': {'ordering': "['group_name']", 'object_name': 'ScheduleGroup', 'db_table': "'bhp_visit_schedulegroup'"},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'group_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'}),
            'grouping_key': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'membership_form': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['visit_schedule.MembershipForm']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'visit_schedule.visitdefinition': {
            'Meta': {'ordering': "['code', 'time_point']", 'object_name': 'VisitDefinition', 'db_table': "'bhp_visit_visitdefinition'"},
            'base_interval': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'base_interval_unit': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '10'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '6', 'db_index': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'grouping': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'instruction': ('django.db.models.fields.TextField', [], {'max_length': '255', 'blank': 'True'}),
            'lower_window': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'lower_window_unit': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '10'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'schedule_group': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['visit_schedule.ScheduleGroup']", 'null': 'True', 'blank': 'True'}),
            'time_point': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '35', 'db_index': 'True'}),
            'upper_window': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'upper_window_unit': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '10'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'visit_tracking_content_type_map': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_content_type_map.ContentTypeMap']", 'null': 'True'})
        }
    }

    complete_apps = ['mpepu_lab']