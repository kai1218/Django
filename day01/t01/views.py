# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from .models import Engineer
# Create your views here.
def index(request):
    return HttpResponse("<h1>Django hahah</h1>")
def my_html(req):
    return render(req,"my_index.html")
def get_data(req):
    data = Engineer.objects.all()
    print(data)
    return render(req,"my_index.html",context={"my_data":data})