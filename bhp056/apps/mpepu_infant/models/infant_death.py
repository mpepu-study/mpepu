from datetime import datetime, time

from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.subject.adverse_event.models import BaseDeathReport

from apps.mpepu.choices import DRUG_RELATIONSHIP

from .infant_off_study_mixin import InfantOffStudyMixin


class InfantDeath (InfantOffStudyMixin, BaseDeathReport):

    death_reason_hospitalized_other = models.TextField(
        verbose_name="6a.i. if other illness or pathogen specify or non infectious reason, please specify below:",
        max_length=250,
        blank=True,
        null=True,
        )
    study_drug_relate = models.CharField(
        verbose_name="7a. Relationship between the participant death and study drug (CTX vs Placebo)",
        max_length=25,
        choices=DRUG_RELATIONSHIP,
        )
    infant_nvp_relate = models.CharField(
        verbose_name="7b. Relationship between the participant death and infant extended nevirapine prophylaxis ",
        max_length=25,
        choices=DRUG_RELATIONSHIP,
        )
    haart_relate = models.CharField(
        verbose_name="7c. Relationship between the participant death and HAART",
        max_length=25,
        choices=DRUG_RELATIONSHIP,
        )
    trad_med_relate = models.CharField(
        verbose_name="7d. Relationship between the participant death and traditional medicine use",
        max_length=25,
        choices=DRUG_RELATIONSHIP,
        )

    history = AuditTrail()

    def get_consenting_subject_identifier(self):
        """Returns mother's identifier."""
        return self.registered_subject.relative_identifier

    def get_report_datetime(self):
        return datetime.combine(self.death_date, time(0, 0))

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantdeath_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Death"