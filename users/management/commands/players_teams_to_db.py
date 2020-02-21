# -*- coding: utf-8 -*-

from .datas_manager import DatasManager
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        datas_from_api = DatasManager()

        

