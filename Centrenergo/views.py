from django.http import HttpResponse, request
from django.shortcuts import render
from django.urls import reverse


def index(request):
    return render(request, 'home/index.html')
