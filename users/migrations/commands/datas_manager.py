# -*- coding: utf-8 -*-

import json
from datetime import date, timedelta, datetime
import wikipedia
import requests

from mainapp.models import Schedule


class DatasManager:
    """ Class for the management of the datas """
    def __init__(self):
        pass

    def get_nba_teams(self):
        """ Get NBA teams list from wikipedia """
        wikipedia.set_lang("en")
        page = wikipedia.page("National_Basketball_Association")
        print(page)


datas = DatasManager()
DatasManager.get_nba_teams(datas)
