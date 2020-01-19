# -*- coding: utf-8 -*-

from .datas_manager import DatasManager
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        datas_from_api = DatasManager()

        season_dates = DatasManager.season_dates(datas_from_api)
        for date in season_dates:

        categories_url_name = DatasManager.category_to_url(datas_from_api, categories_list)
        products_extract = DatasManager.products_extract(datas_from_api, categories_url_name)
        DatasManager.get_products_datas(datas_from_api, products_extract)
