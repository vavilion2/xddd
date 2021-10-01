
from django.db import models

class ZayavkaQuery(models.QuerySet):
    def filter_rab(self,usern):
        return self.filter()


class ZayavkaManager(models.Manager):
    def user_filter(self):
        return self.filter(user__is_rabotyaga=True)