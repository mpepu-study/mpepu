from collections import OrderedDict

from edc.subject.visit_schedule.classes import VisitScheduleConfiguration, site_visit_schedules, EntryTuple, MembershipFormTuple, ScheduleGroupTuple, RequisitionTuple
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
            'title': 'Maternal Post Natal Registration',
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
                RequisitionTuple(100L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'Breast Milk', 'STORAGE', 'BM', SHOW_FORM),
                RequisitionTuple(200L, u'mpepu_lab', u'maternalrequisition', 'PBMC Plasma (STORE ONLY)', 'PBMC Plasma Storage', 'STORAGE', 'WB', SHOW_FORM),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu', SHOW_FORM),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx', SHOW_FORM),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost', SHOW_FORM),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh', SHOW_FORM),
            )}
    visit_definitions['2020M'] = {
            'title': 'Maternal Post Natal Registration',
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
                # (entry_order, app_label, model_name, panel.name, panel.edc_name, panel.panel_type, aliquot_type)
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu', SHOW_FORM),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx', SHOW_FORM),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost', SHOW_FORM),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh', SHOW_FORM),
            )}
    visit_definitions['2030M'] = {
            'title': 'Maternal Post Natal Registration',
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
                RequisitionTuple(10L, u'mpepu_lab', u'maternalrequisition', 'PHS: Ultrasensetive Viral Load', 'Viral load (PHS)', 'TEST', 'WB', SHOW_FORM),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu', SHOW_FORM),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx', SHOW_FORM),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost', SHOW_FORM),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh', SHOW_FORM),
            )}
#     visit_definitions['2030R'] = {
#             'title': 'Maternal ARV Resistance',
#             'time_point': 30,
#             'base_interval': 3,
#             'base_interval_unit': 'M',
#             'window_lower_bound': 0,
#             'window_lower_bound_unit': 'D',
#             'window_upper_bound': 0,
#             'window_upper_bound_unit': 'D',
#             'grouping': 'maternal',
#             'visit_tracking_model': MaternalVisit,
#             'schedule_group': 'Resistance Study',
#             'instructions': None,
#             'requisitions': (
#                              ),
#             'entries': (
#                 #additional forms for the TAB study
#                 EntryTuple(10L, u'mpepu_maternal', u'resistanceeligibility', SHOW_FORM),
#                 EntryTuple(20L, u'mpepu_maternal', u'resistancedisc', SHOW_FORM),
#             )}
    visit_definitions['2060M'] = {
            'title': 'Maternal Post Natal Registration',
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
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu', SHOW_FORM),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx', SHOW_FORM),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost', SHOW_FORM),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh', SHOW_FORM),
            )}
    visit_definitions['2090M'] = {
            'title': 'Maternal Post Natal Registration',
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
                RequisitionTuple(10L, u'mpepu_lab', u'maternalrequisition', 'PHS: Ultrasensetive Viral Load', 'Viral load (PHS)', 'TEST', 'WB', SHOW_FORM),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu', SHOW_FORM),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx', SHOW_FORM),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost', SHOW_FORM),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh', SHOW_FORM),
            )}
    visit_definitions['2120M'] = {
            'title': 'Maternal Post Natal Registration',
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
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu', SHOW_FORM),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx', SHOW_FORM),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost', SHOW_FORM),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh', SHOW_FORM),
            )}
    visit_definitions['2150M'] = {
            'title': 'Maternal Post Natal Registration',
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
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu', SHOW_FORM),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx', SHOW_FORM),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost', SHOW_FORM),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh', SHOW_FORM),
            )}
    visit_definitions['2180M'] = {
            'title': 'Maternal Post Natal Registration',
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
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu', SHOW_FORM),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx', SHOW_FORM),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost', SHOW_FORM),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh', SHOW_FORM),
                EntryTuple(50L, u'mpepu_maternal', u'postnatalinfantfeedingsurvey', SHOW_FORM),
            )}
site_visit_schedules.register(MpepuMaternalPostPartumVisitSchedule)
