from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Schedule
from users.models import Team
from .calendar_insertion import calendar_connection, calendar_insertion, event_insertion


def index(request):
    return render(request, 'mainapp/index.html')


def upload_page(request):
    schedule = Schedule()
    service = calendar_connection()
    calendar_id = calendar_insertion(service)
    teams_list = request.GET.getlist('team')
    for team in teams_list:#works fine
        team_to_insert = get_object_or_404(Team, name=team)
        team_to_insert.favorite.add(request.user)

    schedule_list = Schedule.get_teams_agenda(schedule, teams_list)
    games_list = []

    for schedule_detail in schedule_list:
        for game in schedule_detail:
            game_dict = Schedule.extraction_to_gformat(schedule, game)
            games_list.append(game_dict)
            for game in games_list:
                event_insertion(service, calendar_id, game)

    context = {
        'teams': len(teams_list),
        'games': games_list,
        "service": service,
    }
    return render(request, 'mainapp/upload.html', context)


