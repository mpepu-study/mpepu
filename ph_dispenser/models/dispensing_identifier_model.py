from django.db import models
from bhp_identifier.models import BaseIdentifierModel


class DispensingIdentifierModel(BaseIdentifierModel):

    objects = models.Manager()

    class Meta:
        app_label = "ph_dispenser"
        ordering = ['-created']