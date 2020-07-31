from django.db import models
from core.models import Persona


# Create your models here.
class CaseWorker(Persona):

    def __str__(self):
        return f"{self.gender} {self.last_name}"
