# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from HD.models import Worksheet, Well

# Register your models here.
admin.site.register(Worksheet)
#admin.site.register(Well)

# Display non-default fields in admin view
class WellAdmin(admin.ModelAdmin):
    list_display = ('well_name','worksheet')

admin.site.register(Well, WellAdmin)