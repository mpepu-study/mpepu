from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO

from apps.mpepu_list.models import InfantVaccines

from .base_scheduled_visit_model import BaseScheduledVisitModel
from .infant_fu import InfantFu


class InfantFuMed(BaseScheduledVisitModel):

    infant_fu = models.OneToOneField(InfantFu)

    vaccines_received = models.CharField(
        max_length=25,
        choices=YES_NO,
        verbose_name="since the last attended scheduled visit,did the child recieve any of the following vaccinations",
        help_text="",
        )

    vaccination = models.ManyToManyField(InfantVaccines,
        verbose_name="Vaccines received",
        help_text="Select all the vaccines that were received",
        )

    comments = models.TextField(
        max_length=500,
        verbose_name="Comment",
        blank=True,
        null=True,
        )

    history = AuditTrail()

    def __unicode__(self):
        return "%s" % (self.infant_visit)

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantfumed_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant FollowUp: Medication"
