from django.db.models import Sum

from core.models import Persona


# Create your models here.
class CaseWorker(Persona):

    def __str__(self):
        return f"{self.gender} {self.last_name}"

    def total_support(self):
        amount = self.commitment_set.all().aggregate(sum=Sum('amount'))['sum']
        return amount
