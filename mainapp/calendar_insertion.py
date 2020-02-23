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

    """store = file.Storage('mainapp/token.json')
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
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('mainapp/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
        with open('mainapp/token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service


def calendar_insertion(service):
    calendar = {
        'summary': 'Your NBA team(s) Schedule',
        'timeZone': 'America/New_York'
    }

    created_calendar = service.calendars().insert(body=calendar).execute()

    calendar_id = created_calendar['id']
    return calendar_id


def event_insertion(service, calendar_id, event):
    calendar_list_entry = service.calendarList().get(calendarId=calendar_id).execute()
    if calendar_list_entry['accessRole']:
        event = service.events().insert(calendarId=calendar_id, body=event).execute()
        print(f"The event has been created! View it at {event.get('htmlLink')}!")


