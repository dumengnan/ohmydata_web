#!/usr/bin/env python
__author__ = 'mee'

from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    #t = get_template('current_datetime.html')
    return render_to_response('current_datetime.html',{'current_date':now})

