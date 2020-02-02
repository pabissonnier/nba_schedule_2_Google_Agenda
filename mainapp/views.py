from django.shortcuts import render
from django.http import HttpResponse
from . import users_data


def index(request):
    teams_list = request.GET.getlist('team')
    schedule_list = users_data.get_teams_agenda(teams_list)

    context = {
        'teams': teams_list,
        'schedule': schedule_list,
    }
    return render(request, 'mainapp/index.html', context)

def upload_page(request): #Use this one for upload
    teams_list = request.GET.getlist('team')
    context = {
        'teams': teams_list,
    }
    return render(request, 'mainapp/index.html', context)
