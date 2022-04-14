from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def data(request):
    return HttpResponse ('<h1> DATA ANALYSIS</h1>')