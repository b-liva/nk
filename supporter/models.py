from django.db import models
from core.models import Persona
from caseworker.models import CaseWorker


# Create your models here.
class Supporter(Persona):
    caseworker = models.ForeignKey(CaseWorker, on_delete=models.DO_NOTHING)
    mobile = models.CharField(max_length=15)
