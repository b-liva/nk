from django.contrib import admin

from supporter.models import (
    Supporter,
    Contact,
    FollowUp
)

admin.site.register(Supporter)
admin.site.register(Contact)
admin.site.register(FollowUp)
