# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from HD.models import Worksheet, Well, Sample, Fragment, Allele

# Register your models here.
admin.site.register(Worksheet)
admin.site.register(Sample)
admin.site.register(Allele)

# Display non-default fields in admin view
class WellAdmin(admin.ModelAdmin):
    list_display = ('well_name','worksheet','sample')

admin.site.register(Well, WellAdmin)

class FragmentAdmin(admin.ModelAdmin):
    list_display = ('well','size')

admin.site.register(Fragment, FragmentAdmin)    