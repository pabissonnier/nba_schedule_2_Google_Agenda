from urllib.request import Request

from googleapiclient.discovery import build

from httplib2 import Http
from oauth2client import file, client, tools
from datetime import datetime
from google_auth_oauthlib.flow import InstalledAppFlow
import oauth2client
import allauth
from allauth.socialaccount.models import SocialToken
from oauth2client import file, client
import google.auth.credentials
import pickle
import os.path


def calendar_connection():
    SCOPES = ["https://www.googleapis.com/auth/calendar"]
    flow = InstalledAppFlow.from_client_secrets_file('mainapp/credentials.json', scopes=SCOPES)
    creds = flow.authorized_session()
    user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    creds = client.AccessTokenCredentials(SocialToken.token, user_agent)
    service = build('calendar', 'v3', credentials=creds)
    return service

    """if os.path.exists('mainapp/token.pickle'):
        with open('mainapp/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file('mainapp/credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('mainapp/token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service"""


def check_calendar_exist(service):
    calendar = {
        'summary': 'Your NBA team(s) Schedule',
        'timeZone': 'America/New_York'
    }
    calendar_list = service.calendarList().list().execute()
    for calendar_list_entry in calendar_list['items']:
        if calendar_list_entry['summary'] == calendar['summary']:
            return True
        else:
            return False


def calendar_insertion(service):
    calendar = {
        'summary': 'Your NBA team(s) Schedule',
        'timeZone': 'America/New_York'
    }

    nba_calendar = service.calendars().insert(body=calendar).execute()

    calendar_id = nba_calendar['id']
    return calendar_id


def get_calendar_id(service):
    calendar = {
        'summary': 'Your NBA team(s) Schedule',
        'timeZone': 'America/New_York'
    }
    calendar_list = service.calendarList().list().execute()
    for calendar_list_entry in calendar_list['items']:
        if calendar_list_entry['summary'] == calendar['summary']:
            return calendar_list_entry['id']


def check_event_exist(service, calendar_id, event):
    events = service.events().list(calendarId=calendar_id).execute()
    for element in events['items']:
        if event["summary"] == element["summary"]:
            if event["start"]["dateTime"] == element["start"]["dateTime"]:
                return True
            else:
                return False
        else:
            return False


def event_insertion(service, calendar_id, event):
    page_token = None
    events = service.events().list(calendarId=calendar_id, pageToken=page_token).execute()
    if event in events["items"]:
        pass
    else:
        service.events().insert(calendarId=calendar_id, body=event).execute()
        print(f"The event has been created! View it at {event.get('htmlLink')}!")


