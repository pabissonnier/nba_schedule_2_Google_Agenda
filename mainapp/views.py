from django.shortcuts import render
from django.http import HttpResponse
from . import users_data


def index(request):
    return render(request, 'mainapp/index.html')


def upload_page(request):
    from .test_calendar import test_calendar
    global no_teams
    no_teams = False
    teams_list = request.GET.getlist('team')
    schedule_list = users_data.get_teams_agenda(teams_list)
    events = test_calendar()
    if len(schedule_list) > 0:
        no_teams = False
        context = {
            'teams': teams_list,
            'schedule': schedule_list,
            'noteams': no_teams,
            'events': events,
        }
        return render(request, 'mainapp/upload.html', context)
    else:
        no_teams = True
        message = "Pick one or several teams"
        context = {
            'teams': teams_list,
            'schedule': schedule_list,
            'noteams': no_teams,
            'message': message,
        }
        return render(request, 'mainapp/upload.html', context)
