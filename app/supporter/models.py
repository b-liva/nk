from django.db import models
from django.db.models import Sum, Count
from django.utils.timezone import now

from case.models import Case
from core.models import Persona, TimeStampedModel
from caseworker.models import CaseWorker


# Create your models here.
class Supporter(Persona):
    caseworker = models.ForeignKey(CaseWorker, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.gender} {self.last_name}"

    def total_support(self):
        from commitment.models import Commitment
        amount_total = Commitment.objects.filter(supporter=self).aggregate(sum=Sum('amount'))['sum']
        return amount_total

    def num_cases(self):
        from case.models import Case
        cases_count = Case.objects.filter(commitment__supporter=self).aggregate(count=Count('id'))['count']
        return cases_count


class Contact(TimeStampedModel):
    supporter = models.ForeignKey(Supporter, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"{self.mobile}"


class SuContact(TimeStampedModel):
    supporter = models.ForeignKey(Supporter, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Phone(SuContact):
    phone = models.CharField(max_length=15, null=True, blank=True, unique=True)


class Mobile(SuContact):
    mobile = models.CharField(max_length=15, null=True, blank=True, unique=True)


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


class FollowUp(TimeStampedModel):
    supporter = models.ForeignKey(Supporter, on_delete=models.DO_NOTHING)
    caseworker = models.ForeignKey(CaseWorker, on_delete=models.DO_NOTHING)
    date = models.DateField(default=now)
    case = models.ManyToManyField(Case)
    description = models.TextField(max_length=150)

    def __str__(self):
        return f"{self.supporter} {self.date}"

    def save(self, *args, **kwargs):
        self.caseworker = self.supporter.caseworker
        super(FollowUp, self).save()
