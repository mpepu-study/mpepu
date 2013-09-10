from django.db import models
from audit_trail.audit import AuditTrail
from bhp_sync.models import BaseSyncUuidModel
from bhp_base_model.validators import datetime_not_before_study_start
from bhp_content_type_map.models import ContentTypeMap
from bhp_consent.choices import CONSENT_TYPES
from bhp_consent.managers import ConsentCatalogueManager


class ConsentCatalogue(BaseSyncUuidModel):

    name = models.CharField(
        max_length=50,
        )

    # content_type_map for the consent model
    content_type_map = models.ForeignKey(ContentTypeMap, null=True)

    consent_type = models.CharField(
        max_length=25,
        choices=CONSENT_TYPES,
        )

    version = models.IntegerField()

    start_datetime = models.DateTimeField(
        validators=[datetime_not_before_study_start, ],
        )

    end_datetime = models.DateTimeField(
        validators=[datetime_not_before_study_start, ],
        )

    list_for_update = models.BooleanField(verbose_name='Display for update', default=True)

    add_for_app = models.CharField(
        max_length=25,
        null=True,
        blank=True,
        help_text='If app_name is provided, all models for given app_name will be added to the Attached Models after save. Will not add a model already listed below (no duplicates).',
        )

    history = AuditTrail()

    objects = ConsentCatalogueManager()

    def natural_key(self):
        return (self.name, self.version)
    natural_key.dependencies = ['bhp_content_type_map.contenttypemap']

    def __unicode__(self):
        return '{0} v{1}'.format(self.name, self.version)

    def save(self, *args, **kwargs):
        if self.version == 1 and self.consent_type == 'study':
            self.list_for_update = False
        super(ConsentCatalogue, self).save(*args, **kwargs)

    class Meta:
        app_label = 'bhp_consent'
        unique_together = (('name', 'version'),)
        ordering = ['name', 'version', ]