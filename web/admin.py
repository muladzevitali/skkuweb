from django.contrib import admin

from .models import (Contact, Preset, Notice)

# Register your models here.
admin.site.register(Contact)
admin.site.register(Preset)
admin.site.register(Notice)
