from django.contrib import admin
from bhp_registration.models import RegisteredSubject
from mpepu_infant.models import InfantRandoDeferral, InfantBirth
from mpepu_infant.classes import RegisteredSubjectModelAdmin
from mpepu_infant.forms import InfantRandoDeferralForm


class InfantRandoDeferralAdmin(RegisteredSubjectModelAdmin):
    form = InfantRandoDeferralForm
    date_hierarchy = 'created'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "infant_birth":
            if request.GET.get('subject_identifier'):
                registered_subject = RegisteredSubject.objects.get(subject_identifier=request.GET.get('subject_identifier'))
                kwargs["queryset"] = InfantBirth.objects.filter(registered_subject=registered_subject)
            else:
                kwargs["queryset"] = InfantBirth.objects.none()

        return super(InfantRandoDeferralAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(InfantRandoDeferral, InfantRandoDeferralAdmin)
