from django.shortcuts import render,redirect
from django.http.response import HttpResponse
import json
import hashlib

from django.core import serializers
import os
from datetime import datetime
from django.db import transaction
import uuid
from .models import MachineModel
from django.views.generic import View

# Create your views here.

class Machine(View):
    def get(self, request):
        name = request.data["name"]
        result = MachineModel.objects.create(name='水痕', age= 20)
        print(result[0].age)
        return HttpResponse('hello word')

def index(request):


    return render(request, 'index.html')
    pass

def charts1(request):
    return render(request, 'charts.html')

def charts2(request):
    return render(request, 'charts2.html')

def charts3(request):
    return render(request, 'charts3.html')