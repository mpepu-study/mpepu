from django.db import models
from django.core.urlresolvers import reverse
from bhp_base_model.models import BaseUuidModel
from bhp_visit.models import MembershipForm
from bhp_visit.managers import ScheduleGroupManager


class ScheduleGroup(BaseUuidModel):
    """Model that groups membership forms"""
    group_name = models.CharField(
        max_length=25,
        unique=True
        )

    membership_form = models.ForeignKey(MembershipForm)

    grouping_key = models.CharField(
        max_length=25,
        null=True,
        blank=True,
        help_text=('may specify a common value to group a number of membership forms so '
                  'that when one of the group is keyed, the others are no longer shown.')
        )

    comment = models.CharField(
        max_length=25,
        null=True,
        blank=True
        )

    objects = ScheduleGroupManager()

    def natural_key(self):
        return (self.group_name, )

    def __unicode__(self):
        return unicode(self.group_name)

    def get_absolute_url(self):
        return reverse('admin:bhp_visit_schedulegroup_change', args=(self.id,))

    class Meta:
        ordering = ['group_name']
        app_label = "bhp_visit"