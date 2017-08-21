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

class Sample(models.Model):
    sample_number = models.CharField(max_length=12, null=False, unique=True)

    def __str__(self): # For Python 2, use __unicode__ too
        return self.sample_number

    def __unicode__(self):
        return self.sample_number

class Well(models.Model):
    worksheet = models.ForeignKey(Worksheet)
    sample = models.ForeignKey(Sample)
    well_name = models.CharField(max_length=8, null=False)

    def __str__(self): # For Python 2, use __unicode__ too
        return str(self.worksheet) + " - " + self.well_name

    def __unicode__(self):
        return str(self.worksheet) + " - " + self.well_name


class Allele(models.Model):
    repeats = models.IntegerField(null=False)
    #min_size = models.FloatField()
    #max_size = models.FloatField()

    def __str__(self): # For Python 2, use __unicode__ too
        return str(self.repeats)

    def __unicode__(self):
        return str(self.repeats)


class Fragment(models.Model):
    well = models.ForeignKey(Well)
    allele = models.ForeignKey(Allele)
    dye = models.CharField(max_length=8, null=False)
    size = models.FloatField(null=False)
    height = models.IntegerField(null=False)
    area = models.IntegerField(null=False)
    qual = models.CharField(max_length=8, null=False)
    score = models.IntegerField(null=False)
    comments = models.CharField(max_length=256, null=False)

    def __str__(self): # For Python 2, use __unicode__ too
        return "%s (%s)" % (str(self.size), str(self.allele))

    def __unicode__(self):
        return "%s (%s)" % (str(self.size), str(self.allele))
