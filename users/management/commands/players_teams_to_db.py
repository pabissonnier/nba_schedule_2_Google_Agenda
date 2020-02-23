# -*- coding: utf-8 -*-

from .datas_manager import DatasManager
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        datas = DatasManager()

        # Teams insertion
        json_loads = DatasManager.league_infos_extraction(datas)
        teams_extraction = DatasManager.get_teams_from_json(datas, json_loads)
        DatasManager.team_insertion(datas, teams_extraction)

        # Players insertion
        teams_names = DatasManager.get_teams_names(datas, teams_extraction)
        players_list = DatasManager.get_nba_players(datas, teams_names)
        DatasManager.players_insertion(datas, players_list)

