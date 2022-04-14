from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def us(request):
    return HttpResponse ('This is siam')