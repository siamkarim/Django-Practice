from tkinter.tix import Form

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def machine(request):
    ofer = {"what": "django and machine learning"}
    return render(request,'machine_learning/Machine_learning.html',context=ofer)

