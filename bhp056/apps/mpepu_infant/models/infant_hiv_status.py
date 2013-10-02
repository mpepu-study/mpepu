from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import POS_NEG, YES_NO

from .base_scheduled_visit_model import BaseScheduledVisitModel


class InfantHivStatus(BaseScheduledVisitModel):

    """New form - Infant HIV status - added to 2180 infant visit ONLY """

    recent_hiv_result = models.CharField(
        verbose_name="1. Most recent HIV test result",
        choices=POS_NEG,
        max_length=15,
        help_text="if positive answer Q2, 2a, 2b",
        )
    recent_hiv_date = models.DateField(
        verbose_name="1a. Date of most recent HIV test result",
        )
    recent_hiv_date_est = models.CharField(
        verbose_name="1a)i. Is date of most recent HIV test result ESTIMATED?",
        choices=YES_NO,
        max_length=3,
        )
    test_place = models.TextField(
        verbose_name="1b. Place where HIV test was done:",
        max_length=35,
        )
    result_record = models.CharField(
        verbose_name="1c. Is result written in participants medical record?",
        choices=YES_NO,
        max_length=3,
        )
    date_first_pos = models.DateField(
        verbose_name="2. Date of first positive test",
        help_text="Can only be answered if answer to Q1 is positive",
        null=True,
        blank=True,
        )
    infant_haart = models.CharField(
        verbose_name="2a. Is infant on HAART?",
        choices=YES_NO,
        max_length=3,
        )
    infant_haart_date = models.DateField(
        verbose_name="2b. Date infant started HAART?",
        null=True,
        blank=True,
        )

    history = AuditTrail()

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infanthivstatus_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant HIV status"
