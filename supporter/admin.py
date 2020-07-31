from django.contrib import admin

from supporter.models import (
    Supporter,
    Contact
)

admin.site.register(Supporter)
admin.site.register(Contact)
