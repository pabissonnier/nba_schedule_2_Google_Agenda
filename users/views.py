from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .team_datas import TeamInfos
import wikipedia

from .models import Team, Player


@login_required()
def profile(request):
    return render(request, 'users/profile.html')


@login_required()
def show_favs(request):
    teams_list = Team.objects.filter(favorite=request.user).order_by('name')
    title = "Your favorite team(s)"
    context = {
        'teams_list': teams_list,
        'title': title,
    }
    return render(request, 'users/favs.html', context)

@login_required()
def teams_detail(request, team_id):
    team = get_object_or_404(Team, team_id=team_id)
    players_list = Player.objects.filter(team=team.name).order_by('lastname')
    team_info = TeamInfos()
    team_api_conn = TeamInfos.team_api_connexion(team_info, team_id)
    last_games = TeamInfos.get_infos_from_json(team_info, team_api_conn)

    context = {
        'title': team.name,
        'picture': team.picture,
        'conference': team.conference,
        'division': team.division,
        'players': players_list,
        'last_games': last_games
    }
    return render(request, 'users/detail.html', context)

@login_required()
def player_detail(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    player_name = player.firstname + ' ' + player.lastname
    player_page = wikipedia.page(player_name)
    if player_page:
        player_bio = wikipedia.summary(player_name, sentences=3)

        context = {
            'title': player_name,
            'bio': player_bio,
            'number': player.number,
            'height': player.height,
            'weight': player.weight,
            'position': player.position,
            'college': player.college,
            'debut': player.debut
        }
        return render(request, 'users/player_detail.html', context)
    else:
        pass
