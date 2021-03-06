from django.contrib import admin

from edc.base.modeladmin.admin import BaseModelAdmin, BaseTabularInline

from ..forms import (MaternalPostFuForm, MaternalPostFuDxForm, MaternalPostRegForm, MaternalPostFuDxTForm)
from ..models import (MaternalPostFu, MaternalPostFuDxT, MaternalPostFuDx, MaternalPostReg)

from .maternal_visit_model_admin import MaternalVisitModelAdmin
from .registered_subject_model_admin import RegisteredSubjectModelAdmin


class MyMaternalPostFuModelAdmin (MaternalVisitModelAdmin):

    """ For other sections of MaternalEnroll; that is, related to MaternalPostFu model. """

#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == "maternal_post_fu":
#             kwargs["queryset"] = MaternalPostFu.objects.filter(maternal_visit__appointment__registered_subject__subject_identifier=request.GET.get('subject_identifier', 0),
#                                                                maternal_visit__appointment__visit_definition__code=request.GET.get('visit_code', 0),
#                                                                maternal_visit__appointment__visit_instance=request.GET.get('visit_instance', 0))
#         return super(MyMaternalPostFuModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "maternal_post_fu":
            if request.GET.get('maternal_visit'):
                kwargs["queryset"] = MaternalPostFu.objects.filter(maternal_visit=request.GET.get('maternal_visit'))
        return super(MyMaternalPostFuModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


class MaternalPostFuAdmin(MaternalVisitModelAdmin):

    form = MaternalPostFuForm
    fields = (
        "maternal_visit",
        "mother_weight",
        "enter_weight",
        "bp",
        "breastfeeding",
        "had_mastitis",
        "has_chronic_cond",
        "chronic_cond",
        "chronic_cond_other",
        "started_ctx",
        "comment")
    radio_fields = {
        "mother_weight": admin.VERTICAL,
        "breastfeeding": admin.VERTICAL,
        "had_mastitis": admin.VERTICAL,
        "has_chronic_cond": admin.VERTICAL,
        "started_ctx": admin.VERTICAL}
    filter_horizontal = ("chronic_cond",)
admin.site.register(MaternalPostFu, MaternalPostFuAdmin)


class MaternalPostFuDxTInlineAdmin(BaseTabularInline):

    model = MaternalPostFuDxT
    form = MaternalPostFuDxTForm
    extra = 1


class MaternalPostFuDxTAdmin(BaseModelAdmin):
    form = MaternalPostFuDxTForm
    fields = (
        'post_fu_dx',
        'post_fu_specify',
        'grade',
        'hospitalized'
        )
admin.site.register(MaternalPostFuDxT, MaternalPostFuDxTAdmin)


class MaternalPostFuDxAdmin(MyMaternalPostFuModelAdmin):

    form = MaternalPostFuDxForm
    fields = (
        "maternal_visit",
        "maternal_post_fu",
        "mother_hospitalized",
        "who_clinical_stage",
        "wcs_dx_adult",
        "new_diagnoses")
    radio_fields = {
        "mother_hospitalized": admin.VERTICAL,
        "new_diagnoses": admin.VERTICAL,
        "who_clinical_stage": admin.VERTICAL}
    filter_horizontal = ("wcs_dx_adult",)
    inlines = [MaternalPostFuDxTInlineAdmin, ]

admin.site.register(MaternalPostFuDx, MaternalPostFuDxAdmin)


class MaternalPostRegAdmin(RegisteredSubjectModelAdmin):
    form = MaternalPostRegForm
admin.site.register(MaternalPostReg, MaternalPostRegAdmin)
