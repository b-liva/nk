from django.db import models
from django.utils.timezone import now

from core.models import TimeStampedModel
from supporter.models import Supporter
from case.models import Case
from caseworker.models import CaseWorker
# Create your models here.


class CommitmentAccount(TimeStampedModel):
    title = models.CharField(max_length=15)
    description = models.TextField(max_length=60)

    def __str__(self):
        return self.title


class Commitment(TimeStampedModel):
    supporter = models.ForeignKey(Supporter, on_delete=models.CASCADE)
    caseworkder = models.ForeignKey(CaseWorker, on_delete=models.DO_NOTHING)
    case = models.ForeignKey(Case, on_delete=models.DO_NOTHING)
    amount = models.FloatField(default=0)
    date = models.DateField(default=now)
    account = models.ForeignKey(CommitmentAccount, on_delete=models.DO_NOTHING, default=1)
    report_wanted = models.BooleanField(default=False)
    report_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"supp: {self.supporter.last_name}, recip: {self.case.recipient.first_name}, amount: {self.amount}"

    def save(self, *args, **kwargs):
        self.caseworkder = self.supporter.caseworker
        super(Commitment, self).save()

