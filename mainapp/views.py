from django.shortcuts import render
from django.http import HttpResponse
from . import users_data
from .models import Schedule


def index(request):
    return render(request, 'mainapp/index.html')


def upload_page(request):
    schedule = Schedule()
    global no_teams
    no_teams = False
    teams_list = request.GET.getlist('team')
    schedule_list = Schedule.get_teams_agenda(schedule, teams_list)
    if len(schedule_list) > 0:
        no_teams = False
        games_list = []
        for schedule in schedule_list:
            for game in schedule:
                game_dict = Schedule.extraction_to_gformat(schedule, game, teams_list)
                games_list.append(game_dict)
            context = {
                'teams': teams_list,
                'schedule': schedule_list,
                'noteams': no_teams,
                'games': games_list,
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
