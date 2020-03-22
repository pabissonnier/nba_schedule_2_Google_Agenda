from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import os.path
import pickle


def calendar_connection():
    """ Connection to Google Calendar """
    SCOPES = ["https://www.googleapis.com/auth/calendar"]
    creds = None
    if os.path.exists('mainapp/token.pickle'):
        with open('mainapp/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file('mainapp/credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('mainapp/token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service


def check_calendar_exist(service):
    """ Check if our calendar already exists """
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
    """ If not, we insert our calendar """
    calendar = {
        'summary': 'Your NBA team(s) Schedule',
        'timeZone': 'America/New_York'
    }

    nba_calendar = service.calendars().insert(body=calendar).execute()

    calendar_id = nba_calendar['id']
    return calendar_id


def get_calendar_id(service):
    """ If it exists, we get the existing calendar id """
    calendar = {
        'summary': 'Your NBA team(s) Schedule',
        'timeZone': 'America/New_York'
    }
    calendar_list = service.calendarList().list().execute()
    for calendar_list_entry in calendar_list['items']:
        if calendar_list_entry['summary'] == calendar['summary']:
            return calendar_list_entry['id']


def event_insertion(service, calendar_id, event):
    """ For a game in the schedule, we insert an event """
    service.events().insert(calendarId=calendar_id, body=event).execute()
    print(f"The event has been created! View it at {event.get('htmlLink')}!")


