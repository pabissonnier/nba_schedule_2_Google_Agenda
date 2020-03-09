from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Schedule
from users.models import Team
from .calendar_insertion import calendar_connection, calendar_insertion, event_insertion, \
    check_calendar_exist, get_calendar_id


def index(request):
    return render(request, 'mainapp/index.html')


def upload_page(request):
    w_teams = Team.objects.filter(conference="West").order_by('name')
    e_teams = Team.objects.filter(conference="East").order_by('name')
    teams_list = request.GET.getlist('team')
    if teams_list:
        schedule = Schedule()
        service = calendar_connection()
        has_agenda = check_calendar_exist(service)

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

        subject = "Merci pour votre inscription !"
        message = 'Hello {0} !,\n\n' \
                  'Nous sommes ravis de vous compter parmi nos utilisateurs :) ' \
                  'Vous pouvez désormais ajouter des produits à votre liste de favoris...\n\n' \
                  'A bientôt chez Purbeurre'.format(request.user.username)
        from_email = settings.EMAIL_HOST_USER
        to_user = [request.user.email]
        send_mail(subject, message, from_email, to_user, fail_silently=True)

        messages.success(request, f'Schedules successfully uploaded, check your Google Calendar')

    context = {
        'w_teams': w_teams,
        'e_teams': e_teams,
    }

    return render(request, 'mainapp/upload.html', context)




