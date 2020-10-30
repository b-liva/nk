from django.db import models
from django.utils import timezone


# Create your models here.
class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides selfupdating ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(TimeStampedModel, self).save(*args, **kwargs)


class Gender(models.Model):
    gender_type = models.CharField(max_length=10)
    title = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.title}"


class Persona(TimeStampedModel):
    gender = models.ForeignKey(Gender, on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

