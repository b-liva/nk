from django.db import models
from django.db.models import Sum, F

from core.models import TimeStampedModel, Persona


# Create your models here.
class Recipient(Persona):

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def total_cases(self):
        case_count = self.case_set.all().count()
        return case_count

    def total_amount(self):
        from commitment.models import Commitment
        supports_amount = Commitment.objects.filter(case__recipient=self).aggregate(sum=Sum('amount'))['sum']
        return supports_amount

