from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Schedule
from users.models import Team
from .calendar_insertion import calendar_connection, calendar_insertion, event_insertion, \
    check_calendar_exist, get_calendar_id


def index(request):
    return render(request, 'mainapp/index.html')


def upload_page(request):
    schedule = Schedule()
    service = calendar_connection()

    has_agenda = check_calendar_exist(service)
    teams_list = request.GET.getlist('team')
    if not has_agenda:
        calendar_id = calendar_insertion(service)
    else:
        calendar_id = get_calendar_id(service)

    for team in teams_list:
        team_to_insert = get_object_or_404(Team, name=team)
        team_to_insert.favorite.add(request.user)

    schedule_list = Schedule.get_teams_agenda(schedule, teams_list)
    for schedule_detail in schedule_list:
        game_list = []
        for game in schedule_detail:
            game_dict = Schedule.extraction_to_gformat(schedule, game)
            game_list.append(game_dict)
        for event in game_list:
            event_insertion(service, calendar_id, event)

    context = {
        'teams': len(teams_list),
        "service": service,
    }
    return render(request, 'mainapp/upload.html', context)




