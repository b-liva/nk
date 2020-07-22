from django.contrib import admin

from supporter.models import (
    Gender,
    Supporter
)

admin.site.register(Gender)
admin.site.register(Supporter)
