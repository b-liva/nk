from django.db import models
from django.utils.timezone import now
from core.models import Persona, TimeStampedModel
from caseworker.models import CaseWorker


# Create your models here.
class Supporter(Persona):
    caseworker = models.ForeignKey(CaseWorker, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.gender} {self.last_name}"


class Contact(TimeStampedModel):
    supporter = models.ForeignKey(Supporter, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"{self.mobile}"


class SupporterCwChange(TimeStampedModel):
    supporter = models.ForeignKey(Supporter, on_delete=models.CASCADE)
    prev_cw = models.ForeignKey(CaseWorker, on_delete=models.CASCADE, related_name='prev_ce')
    new_cw = models.ForeignKey(CaseWorker, on_delete=models.CASCADE)
    date = models.DateField(default=now)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(SupporterCwChange, self).save(force_insert, force_update, using, update_fields)
    #     # self.prev_cw = self.supporter.caseworker
        self.supporter.caseworker = self.new_cw
        self.supporter.save()
