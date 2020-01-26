from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'mainapp/index.html')


def upload_page(request):
    return render(request, 'mainapp/upload.html')
