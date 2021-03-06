from django.db import models


class AeManager(models.Manager):

    def get_by_natural_key(self, report_datetime, tracking_identifier):
        return self.get(
            report_datetime=report_datetime,
            ae_initial__tracking_identifier=tracking_identifier)
