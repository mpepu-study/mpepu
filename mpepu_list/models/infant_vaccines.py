from bhp_base_model.models import BaseListModel


class InfantVaccines (BaseListModel):

    class Meta:
        app_label = "mpepu_list"
        verbose_name = "Infant Vaccinations"
