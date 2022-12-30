from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

def root(request):
    return HttpResponse("The server has started")