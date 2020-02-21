# -*- coding: utf-8 -*-

from .datas_manager import DatasManager
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        datas_from_api = DatasManager()

        season_dates = DatasManager.season_dates(datas_from_api)
        for date in season_dates:
            day_schedule = DatasManager.games_extraction(datas_from_api, date)
            day_infos = DatasManager.get_infos_from_json(datas_from_api, day_schedule)
            day_infos_converted = DatasManager.date_converter(datas_from_api, day_infos)
            DatasManager.game_day_insertion(datas_from_api, day_infos_converted)
