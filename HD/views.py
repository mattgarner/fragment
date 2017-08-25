# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from HD.models import Worksheet, Well, Fragment
from django.template import RequestContext
from django.core.urlresolvers import reverse

from HD.models import Genemarker_data
from HD.forms import Genemarker_dataForm  # Ugh, underscores and Camelback
import json

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

def genemarker_upload(request):
    # Upload
    if request.method == "POST":
        form = Genemarker_dataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('datasub'))

    else:
        form = Genemarker_dataForm()

    gm_files = Genemarker_data.objects.order_by('-upload_date')
    context_dict = {"gm_files":gm_files,
                    "form":form}
    return render(request, 'HD/upload.html', context_dict)

from graphos.sources.model import ModelDataSource
from graphos.renderers import flot, gchart

def fplot(request):
    
    queryset = Fragment.objects.all()
    data_source = ModelDataSource(queryset,
                                  fields=['size', 'area', 'height'])
    line_fchart = flot.LineChart(data_source,
                                  options={'title': "Test Title"})
    #column_chart = self.renderer.ColumnChart(simple_data_source,
    #                                  options={'title': "Sales/ Expense"})
    #bar_chart = self.renderer.BarChart(data_source,
    #                            options={'title': "Expense Growth"})
    #pie_chart = self.renderer.PieChart(data_source)

    context_dict = {
            "fchart": line_fchart,
            #"column_chart": column_chart,
            #'bar_chart': bar_chart,
            #'pie_chart': pie_chart,
            }

    return render(request, "HD/fplot.html", context_dict)

from graphos.sources.simple import SimpleDataSource
from graphos.renderers.gchart import LineChart

def gplot(request):

    queryset = Fragment.objects.all()
    data_source = ModelDataSource(queryset,
                                  fields=['size', 'area', 'height'])
    line_gchart = gchart.LineChart(data_source,
                                  options={'title': "Test Title"})

    context_dict = {
            "gchart": line_gchart,
            #"column_chart": column_chart,
            #'bar_chart': bar_chart,
            #'pie_chart': pie_chart,
            }

    return render(request, "HD/fplot.html", context_dict)