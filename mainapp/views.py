from django.shortcuts import render, redirect
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
    global game_list, schedule_list, schedule_detail
    w_teams = Team.objects.filter(conference="West").order_by('name')
    e_teams = Team.objects.filter(conference="East").order_by('name')
    teams_list = request.GET.getlist('team')
    if request.method == 'GET':
        if teams_list:
            if len(teams_list) > 0:
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
                game_list = []
                for schedule_detail in schedule_list:
                    for game in schedule_detail:
                        game_id = game.id
                        game_list.append(game_id)
                    game_list = list(dict.fromkeys(game_list))
                game_list_final = []
                try:
                    for game_id in game_list:
                        game = Schedule.objects.get(id=game_id)
                        game_dict = Schedule.extraction_to_gformat(schedule, game)
                        game_list_final.append(game_dict)

                    for event in game_list_final:
                        event_insertion(service, calendar_id, event)

                    messages.success(request, f'Schedules successfully uploaded, check your Google Calendar')
                    subject = "Your NBA schedules"
                    message = 'Hello {0},\n\n' \
                              'Your NBA team(s) schedule is now updloaded to your Google Agenda ! ' \
                              'Please check your agenda to see them, if you want to erase them, please go to your calendar and' \
                              'remove the "Your NBA team(s) Schedule" calendar. Afterwards you can recreate an agenda on our' \
                              'website.\n\n' \
                              'See you soon !'.format(request.user.username.title())
                    from_email = settings.EMAIL_HOST_USER
                    to_list = [request.user.email, settings.EMAIL_HOST_USER]
                    send_mail(subject, message, from_email, to_list, fail_silently=False)
                    return redirect('upload')
                except:
                    messages.warning(request, f"Schedules couldn't be uploaded, please try later")

            if len(teams_list) == 0:
                messages.warning(request, f"Please select at least one team")
                context = {
                    'w_teams': w_teams,
                    'e_teams': e_teams
                }

                return render(request, 'mainapp/upload.html', context)

        context = {
            'w_teams': w_teams,
            'e_teams': e_teams
        }

        return render(request, 'mainapp/upload.html', context)





