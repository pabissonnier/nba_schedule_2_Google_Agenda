from django.shortcuts import render
from django.http import HttpResponse
from . import users_data


def index(request):
    teams_list = request.GET.getlist('team')
    context = {
        'teams': teams_list,
    }
    return render(request, 'mainapp/index.html', context)


