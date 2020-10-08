from django.db import models
from django.db.models import Sum
from django.utils.timezone import now

from core.models import TimeStampedModel
from recipient.models import Recipient


class Illness(TimeStampedModel):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title}"


class Case(TimeStampedModel):
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE)
    illness = models.ManyToManyField(Illness)
    description = models.TextField(max_length=1000, blank=True, null=True)
    date = models.DateField(default=now)

    def __str__(self):
        return f"{self.recipient.first_name} {self.recipient.last_name}: {self.illness.count()}"

    def total_amount(self):
        amount = self.commitment_set.aggregate(sum=Sum('amount'))['sum']
        return amount




