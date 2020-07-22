from django.db import models
from django.utils import timezone
from core.models import TimeStampedModel


class Gender(models.Model):
    gender_type = models.CharField(max_length=10)
    title = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.title}"


# Create your models here.
class Supporter(TimeStampedModel):
    gender = models.ForeignKey(Gender, on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=15)

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Supporter, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
