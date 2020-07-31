from django.db import models
from core.models import Persona, TimeStampedModel
from caseworker.models import CaseWorker


# Create your models here.
class Supporter(Persona):
    caseworker = models.ForeignKey(CaseWorker, on_delete=models.DO_NOTHING)


class Contact(TimeStampedModel):
    supporter = models.ForeignKey(Supporter, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"{self.mobile}"


