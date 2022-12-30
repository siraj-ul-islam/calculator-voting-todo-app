from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *
from django.http import HttpResponse, JsonResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def submit(request):
    pass