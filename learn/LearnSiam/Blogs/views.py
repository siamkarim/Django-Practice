from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def blog1(request):
    return HttpResponse('This is Bloggs one')
