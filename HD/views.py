# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from HD.models import Worksheet, Well, Fragment

def index(request):
    context_dict = {'boldmessage':'INDEX PAGE'}
    return render(request, 'HD/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage':'ABOUT PAGE'}
    return render(request, 'HD/about.html', context=context_dict)

def submit_data(request):
    context_dict = {'boldmessage':'Data Submission'}
    return render(request, 'HD/index.html', context=context_dict)

def view_data(request):
    context_dict = {'boldmessage':'Data View'}
    return render(request, 'HD/index.html', context=context_dict)

def worksheet_list(request):
    worksheet_list = Worksheet.objects.order_by("ws_number")
    context_dict = {"worksheets":worksheet_list}
    return render(request, "HD/worksheets.html", context_dict)

def well_list(request):
    well_list = [str(well) for well in Well.objects.order_by("worksheet")]
    context_dict = {"wells":well_list}
    return render(request, "HD/wells.html", context_dict)

def show_worksheet(request, ws_number_slug):
    context_dict = {}
    try:
        worksheet = Worksheet.objects.get(slug=ws_number_slug)
        wells = Well.objects.filter(worksheet=worksheet)
        context_dict["wells"] = wells
        context_dict["worksheet"] = worksheet
    except Worksheet.DoesNotExist:
        context_dict["wells"] = None
        context_dict["worksheet"] = None

    return render(request, "HD/worksheet.html", context_dict)

def show_well(request, well_name, ws_number_slug):
    context_dict = {}
    well_name = well_name.upper()
    
    try:
        worksheet = Worksheet.objects.get(slug=ws_number_slug)
        well = Well.objects.get(well_name=well_name, worksheet=worksheet)
        fragments = Fragment.objects.filter(well=well)
        
        context_dict["worksheet"] = worksheet
        context_dict["well"] = well
        context_dict["fragments"] = fragments
    
    except (Worksheet.DoesNotExist, Well.DoesNotExist, Fragment.DoesNotExist):
        context_dict["worksheet"] = None
        context_dict["well"] = None
        context_dict["fragments"] = None

    return render(request, "HD/well.html", context_dict)