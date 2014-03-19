from collections import OrderedDict

from edc.subject.visit_schedule.classes import VisitScheduleConfiguration, site_visit_schedules, EntryTuple, MembershipFormTuple, ScheduleGroupTuple, RequisitionPanelTuple
from edc.utils.constants import SHOW_FORM, HIDE_FORM

from ..models import MaternalVisit, MaternalPostReg


class MpepuMaternalPostPartumVisitSchedule(VisitScheduleConfiguration):

    name = 'postreg visit schedule'
    app_label = 'mpepu_maternal'
    # membership forms
    # (name, model, visible)
    membership_forms = OrderedDict({
        'maternal_postnatal_reg': MembershipFormTuple('maternal_postnatal_reg', MaternalPostReg, True),
#         'maternal_resistance': MembershipFormTuple('maternal_resistance', ResistanceConsent, True),
        })

    # schedule groups
    # (name, membership_form_name, grouping_key, comment)
    schedule_groups = OrderedDict({
        'Post Partum Follow-up': ScheduleGroupTuple('Post Partum Follow-up', 'maternal_postnatal_reg', None, None),
#         'Resistance Study': ScheduleGroupTuple('Resistance Study', 'maternal_resistance', None, None),
        })
    # visit_schedule
    # see edc.subject.visit_schedule.models.visit_defintion
    visit_definitions = OrderedDict()

    visit_definitions['2010M'] = {
            'title': 'Infant Randomization',
            'time_point': 10,
            'base_interval': 1,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': MaternalVisit,
            'schedule_group': 'Maternal Post Partum Reg',
            'instructions': None,
            'requisitions': (
                # (entry_order, app_label, model_name, panel.name, panel.edc_name, panel.panel_type, aliquot_type)
                RequisitionPanelTuple(100L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'STORAGE', 'BM', SHOW_FORM),
                RequisitionPanelTuple(200L, u'mpepu_lab', u'maternalrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', SHOW_FORM),
                RequisitionPanelTuple(300L, u'mpepu_lab', u'maternalrequisition', 'Hematology (ARV)', 'TEST', 'WB', HIDE_FORM),
                RequisitionPanelTuple(400L, u'mpepu_lab', u'maternalrequisition', 'Viral load (storage only)', 'STORAGE', 'WB', HIDE_FORM),
                RequisitionPanelTuple(500L, u'mpepu_lab', u'maternalrequisition', 'CD4 (ARV)', 'TEST', 'WB', HIDE_FORM),
                RequisitionPanelTuple(600L, u'mpepu_lab', u'maternalrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', HIDE_FORM),
                RequisitionPanelTuple(700L, u'mpepu_lab', u'maternalrequisition', 'PHS: Ultrasensetive Viral Load', 'TEST', 'WB', HIDE_FORM),
                RequisitionPanelTuple(800L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'TEST', 'WB', HIDE_FORM),
                RequisitionPanelTuple(900L, u'mpepu_lab', u'maternalrequisition', 'PHS: Ultrasensetive Viral Load', 'TEST', 'WB', HIDE_FORM),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu', SHOW_FORM),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx', SHOW_FORM),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost', SHOW_FORM),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh', SHOW_FORM),
            )}
    visit_definitions['2020M'] = {
            'title': '2 Months Postpartum Visit',
            'time_point': 20,
            'base_interval': 2,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': MaternalVisit,
            'schedule_group': 'Maternal Post Partum Reg',
            'instructions': None,
            'requisitions': (
                # (entry_order, app_label, model_name, requisition_panel_name, panel.panel_type, aliquot_type)
                RequisitionPanelTuple(100L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'STORAGE', 'BM', HIDE_FORM),
                RequisitionPanelTuple(200L, u'mpepu_lab', u'maternalrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', HIDE_FORM),
                RequisitionPanelTuple(300L, u'mpepu_lab', u'maternalrequisition', 'Hematology (ARV)', 'TEST', 'WB', HIDE_FORM),
                RequisitionPanelTuple(400L, u'mpepu_lab', u'maternalrequisition', 'Viral load (storage only)', 'STORAGE', 'WB', HIDE_FORM),
                RequisitionPanelTuple(500L, u'mpepu_lab', u'maternalrequisition', 'CD4 (ARV)', 'TEST', 'WB', HIDE_FORM),
                RequisitionPanelTuple(600L, u'mpepu_lab', u'maternalrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', HIDE_FORM),
                RequisitionPanelTuple(700L, u'mpepu_lab', u'maternalrequisition', 'PHS: Ultrasensetive Viral Load', 'TEST', 'WB', HIDE_FORM),
                RequisitionPanelTuple(800L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'TEST', 'WB', HIDE_FORM),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu', SHOW_FORM),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx', SHOW_FORM),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost', SHOW_FORM),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh', SHOW_FORM),
            )}
    visit_definitions['2030M'] = {
            'title': '3 Months Postpartum Visit',
            'time_point': 30,
            'base_interval': 3,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': MaternalVisit,
            'schedule_group': 'Maternal Post Partum Reg',
            'instructions': None,
            'requisitions': (
                # (entry_order, app_label, model_name, panel.name, panel.edc_name, panel.panel_type, aliquot_type)
                RequisitionPanelTuple(10L, u'mpepu_lab', u'maternalrequisition', 'PHS: Ultrasensetive Viral Load', 'TEST', 'WB', SHOW_FORM),
                RequisitionPanelTuple(100L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'STORAGE', 'BM', HIDE_FORM),
                RequisitionPanelTuple(200L, u'mpepu_lab', u'maternalrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', HIDE_FORM),
                RequisitionPanelTuple(300L, u'mpepu_lab', u'maternalrequisition', 'Hematology (ARV)', 'TEST', 'WB', HIDE_FORM),
                RequisitionPanelTuple(400L, u'mpepu_lab', u'maternalrequisition', 'Viral load (storage only)', 'STORAGE', 'WB', HIDE_FORM),
                RequisitionPanelTuple(500L, u'mpepu_lab', u'maternalrequisition', 'CD4 (ARV)', 'TEST', 'WB', HIDE_FORM),
                RequisitionPanelTuple(600L, u'mpepu_lab', u'maternalrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', HIDE_FORM),
                RequisitionPanelTuple(800L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'TEST', 'WB', HIDE_FORM),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu', SHOW_FORM),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx', SHOW_FORM),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost', SHOW_FORM),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh', SHOW_FORM),
            )}
    visit_definitions['2060M'] = {
            'title': '6 Months Postpartum Visit',
            'time_point': 60,
            'base_interval': 6,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': MaternalVisit,
            'schedule_group': 'Maternal Post Partum Reg',
            'instructions': None,
            'requisitions': (
                # (entry_order, app_label, model_name, panel.name, panel.edc_name, panel.panel_type, aliquot_type)
                RequisitionPanelTuple(10L, u'mpepu_lab', u'maternalrequisition', 'PHS: Ultrasensetive Viral Load', 'TEST', 'WB', HIDE_FORM),
                RequisitionPanelTuple(100L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'STORAGE', 'BM', HIDE_FORM),
                RequisitionPanelTuple(200L, u'mpepu_lab', u'maternalrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', HIDE_FORM),
                RequisitionPanelTuple(300L, u'mpepu_lab', u'maternalrequisition', 'Hematology (ARV)', 'TEST', 'WB', HIDE_FORM),
                RequisitionPanelTuple(400L, u'mpepu_lab', u'maternalrequisition', 'Viral load (storage only)', 'STORAGE', 'WB', HIDE_FORM),
                RequisitionPanelTuple(500L, u'mpepu_lab', u'maternalrequisition', 'CD4 (ARV)', 'TEST', 'WB', HIDE_FORM),
                RequisitionPanelTuple(600L, u'mpepu_lab', u'maternalrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', HIDE_FORM),
                RequisitionPanelTuple(800L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'TEST', 'WB', HIDE_FORM),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu', SHOW_FORM),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx', SHOW_FORM),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost', SHOW_FORM),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh', SHOW_FORM),
            )}
    visit_definitions['2090M'] = {
            'title': '9 Months Postpartum Visit',
            'time_point': 10,
            'base_interval': 1,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': MaternalVisit,
            'schedule_group': 'Maternal Post Partum Reg',
            'instructions': None,
            'requisitions': (
                # (entry_order, app_label, model_name, panel.name, panel.edc_name, panel.panel_type, aliquot_type)
                RequisitionPanelTuple(10L, u'mpepu_lab', u'maternalrequisition', 'PHS: Ultrasensetive Viral Load', 'TEST', 'WB', SHOW_FORM),
                RequisitionPanelTuple(100L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'STORAGE', 'BM', HIDE_FORM),
                RequisitionPanelTuple(200L, u'mpepu_lab', u'maternalrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', HIDE_FORM),
                RequisitionPanelTuple(300L, u'mpepu_lab', u'maternalrequisition', 'Hematology (ARV)', 'TEST', 'WB', HIDE_FORM),
                RequisitionPanelTuple(400L, u'mpepu_lab', u'maternalrequisition', 'Viral load (storage only)', 'STORAGE', 'WB', HIDE_FORM),
                RequisitionPanelTuple(500L, u'mpepu_lab', u'maternalrequisition', 'CD4 (ARV)', 'TEST', 'WB', HIDE_FORM),
                RequisitionPanelTuple(600L, u'mpepu_lab', u'maternalrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', HIDE_FORM),
                RequisitionPanelTuple(800L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'TEST', 'WB', HIDE_FORM),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu', SHOW_FORM),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx', SHOW_FORM),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost', SHOW_FORM),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh', SHOW_FORM),
            )}
    visit_definitions['2120M'] = {
            'title': '12 Months Postpartum Visit',
            'time_point': 120,
            'base_interval': 12,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': MaternalVisit,
            'schedule_group': 'Maternal Post Partum Reg',
            'instructions': None,
            'requisitions': (
                # (entry_order, app_label, model_name, panel.name, panel.edc_name, panel.panel_type, aliquot_type)
                RequisitionPanelTuple(10L, u'mpepu_lab', u'maternalrequisition', 'PHS: Ultrasensetive Viral Load', 'TEST', 'WB', HIDE_FORM),
                RequisitionPanelTuple(100L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'STORAGE', 'BM', HIDE_FORM),
                RequisitionPanelTuple(200L, u'mpepu_lab', u'maternalrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', HIDE_FORM),
                RequisitionPanelTuple(300L, u'mpepu_lab', u'maternalrequisition', 'Hematology (ARV)', 'TEST', 'WB', HIDE_FORM),
                RequisitionPanelTuple(400L, u'mpepu_lab', u'maternalrequisition', 'Viral load (storage only)', 'STORAGE', 'WB', HIDE_FORM),
                RequisitionPanelTuple(500L, u'mpepu_lab', u'maternalrequisition', 'CD4 (ARV)', 'TEST', 'WB', HIDE_FORM),
                RequisitionPanelTuple(600L, u'mpepu_lab', u'maternalrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', HIDE_FORM),
                RequisitionPanelTuple(800L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'TEST', 'WB', HIDE_FORM),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu', SHOW_FORM),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx', SHOW_FORM),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost', SHOW_FORM),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh', SHOW_FORM),
            )}
    visit_definitions['2150M'] = {
            'title': '15 Months Postpartum Visit',
            'time_point': 150,
            'base_interval': 15,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': MaternalVisit,
            'schedule_group': 'Maternal Post Partum Reg',
            'instructions': None,
            'requisitions': (
                # (entry_order, app_label, model_name, panel.name, panel.edc_name, panel.panel_type, aliquot_type)
                RequisitionPanelTuple(10L, u'mpepu_lab', u'maternalrequisition', 'PHS: Ultrasensetive Viral Load', 'TEST', 'WB', HIDE_FORM),
                RequisitionPanelTuple(100L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'STORAGE', 'BM', HIDE_FORM),
                RequisitionPanelTuple(200L, u'mpepu_lab', u'maternalrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', HIDE_FORM),
                RequisitionPanelTuple(300L, u'mpepu_lab', u'maternalrequisition', 'Hematology (ARV)', 'TEST', 'WB', HIDE_FORM),
                RequisitionPanelTuple(400L, u'mpepu_lab', u'maternalrequisition', 'Viral load (storage only)', 'STORAGE', 'WB', HIDE_FORM),
                RequisitionPanelTuple(500L, u'mpepu_lab', u'maternalrequisition', 'CD4 (ARV)', 'TEST', 'WB', HIDE_FORM),
                RequisitionPanelTuple(600L, u'mpepu_lab', u'maternalrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', HIDE_FORM),
                RequisitionPanelTuple(800L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'TEST', 'WB', HIDE_FORM),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu', SHOW_FORM),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx', SHOW_FORM),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost', SHOW_FORM),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh', SHOW_FORM),
            )}
    visit_definitions['2180M'] = {
            'title': '18 Months Postpartum Visit',
            'time_point': 10,
            'base_interval': 1,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': MaternalVisit,
            'schedule_group': 'Maternal Post Partum Reg',
            'instructions': None,
            'requisitions': (
                # (entry_order, app_label, model_name, panel.name, panel.edc_name, panel.panel_type, aliquot_type)
                RequisitionPanelTuple(10L, u'mpepu_lab', u'maternalrequisition', 'PHS: Ultrasensetive Viral Load', 'TEST', 'WB', HIDE_FORM),
                RequisitionPanelTuple(100L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'STORAGE', 'BM', HIDE_FORM),
                RequisitionPanelTuple(200L, u'mpepu_lab', u'maternalrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', HIDE_FORM),
                RequisitionPanelTuple(300L, u'mpepu_lab', u'maternalrequisition', 'Hematology (ARV)', 'TEST', 'WB', HIDE_FORM),
                RequisitionPanelTuple(400L, u'mpepu_lab', u'maternalrequisition', 'Viral load (storage only)', 'STORAGE', 'WB', HIDE_FORM),
                RequisitionPanelTuple(500L, u'mpepu_lab', u'maternalrequisition', 'CD4 (ARV)', 'TEST', 'WB', HIDE_FORM),
                RequisitionPanelTuple(600L, u'mpepu_lab', u'maternalrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', HIDE_FORM),
                RequisitionPanelTuple(800L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'TEST', 'WB', HIDE_FORM),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu', SHOW_FORM),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx', SHOW_FORM),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost', SHOW_FORM),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh', SHOW_FORM),
                EntryTuple(50L, u'mpepu_maternal', u'postnatalinfantfeedingsurvey', SHOW_FORM),
            )}
site_visit_schedules.register(MpepuMaternalPostPartumVisitSchedule)
