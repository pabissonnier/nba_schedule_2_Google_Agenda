from django.shortcuts import render
from django.http import HttpResponse
from .models import Schedule
from .calendar_insertion import calendar_connection, calendar_insertion, event_insertion


def index(request):
    return render(request, 'mainapp/index.html')


def upload_page(request):
    schedule = Schedule()
    teams_list = request.GET.getlist('team')
    schedule_list = Schedule.get_teams_agenda(schedule, teams_list)
    games_list = []
    service = calendar_connection()
    calendar_id = calendar_insertion(service)
    for schedule in schedule_list:
        for game in schedule:
            game_dict = Schedule.extraction_to_gformat(schedule, game, teams_list)
            games_list.append(game_dict)
            for game in games_list:
                event_insertion(service, calendar_id, game)

    context = {
        'teams': teams_list,
        'schedule': len(schedule_list),
        'games': len(games_list),
        #"service": service,
        #'calendar_id': calendar_id,
    }
    return render(request, 'mainapp/upload.html', context)

