from django.contrib import admin
from checkin_app.models import Child, Pin, Profile

# Register your models here.
admin.site.register([Child, Pin, Profile])
