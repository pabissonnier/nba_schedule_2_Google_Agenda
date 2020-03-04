from urllib.request import Request

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from datetime import datetime
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
import os.path


def calendar_connection():
    SCOPES = "https://www.googleapis.com/auth/calendar"

    """store = file.Storage('mainapp/token.pickle')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('mainapp/credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))
    return service"""

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('mainapp/token.pickle'):
        with open('mainapp/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file('mainapp/credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
        with open('mainapp/token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service


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


def check_event_exist(service, calendar_id, event_start, event_summary):
    event_list = service.events().list(calendarId=calendar_id).execute()
    for event_list_entry in event_list['items']:
        if event_list_entry['summary'] == event_summary and event_list_entry['start']['dateTime'] == event_start:
            return True
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


