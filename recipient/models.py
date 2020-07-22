from django.db import models
from core.models import TimeStampedModel


class Illness(TimeStampedModel):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title}"


# Create your models here.
class Recipient(TimeStampedModel):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    illness = models.ForeignKey(Illness, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"