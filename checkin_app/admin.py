from django.contrib import admin
from checkin_app.models import Child, Profile, Time

# Register your models here.
admin.site.register([Child, Profile, Time])
