# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

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