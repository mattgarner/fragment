# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Worksheet(models.Model):
    ws_number = models.CharField(max_length=16, unique=True, null=False)
    datetime = models.DateTimeField(null=True, unique=True)
    #project_path = models.FilePathField(allow_files=True)
    panel = models.CharField(max_length=32, unique=False, null=False)
    size = models.CharField(max_length=16, unique=False, null=False)
    analysis_type = models.CharField(max_length=32, unique=False, null=False)
    software = models.CharField(max_length=128, unique=False, null=False)

    def __str__(self): # For Python 2, use __unicode__ too
        return self.ws_number

    def __unicode__(self):
        return self.ws_number

class Well(models.Model):
    worksheet_id = models.ForeignKey(Worksheet)
    well_name = models.CharField(max_length=8, null=False)
    #s_id = models.ForeignKey(Sample)
    #wn_id = models.ForeignKey(Well_name)

    def __str__(self): # For Python 2, use __unicode__ too
        return self.name

    def __unicode__(self):
        return self.name