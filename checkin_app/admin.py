from django.contrib import admin
from checkin_app.models import Child, Profile

# Register your models here.
admin.site.register([Child, Profile])
