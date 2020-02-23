from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .models import Team


@login_required()
def profile(request):
    return render(request, 'users/profile.html')


""""@login_required()
def favs(request):
    team = get_object_or_404(Team, id=request.POST.get('fav-btn'))
    team.favorite.add(request.user)
    return redirect(request.META['HTTP_REFERER']"""


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
def teams_detail(request, team_name):
    team = get_object_or_404(Team, name=team_name)

    context = {
        'title': team.name,
        'picture': team.picture,
        'conference': team.conference,
        'division': team.division,
    }
    return render(request, 'users/detail.html', context)
