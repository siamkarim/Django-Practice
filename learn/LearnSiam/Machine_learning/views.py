from tkinter.tix import Form

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def machine(request):
    return HttpResponse('<h1> This is my first attempt to learn Django </h1>')

def deep (request):
    return HttpResponse('<h1> This is my first attempt to deep learning</h1>')    