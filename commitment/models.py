from django.db import models
from core.models import TimeStampedModel
from supporter.models import Supporter
from case.models import Case
# Create your models here.


class Commitment(TimeStampedModel):
    supporter = models.ForeignKey(Supporter, on_delete=models.CASCADE)
    case = models.ForeignKey(Case, on_delete=models.DO_NOTHING)
    amount = models.FloatField(default=0)

    def __str__(self):
        return f"supp: {self.supporter.last_name}, recip: {self.case.recipient.first_name}, amount: {self.amount}"

