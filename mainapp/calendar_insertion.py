from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from datetime import datetime


def calendar_connection():
    SCOPES = "https://www.googleapis.com/auth/calendar"
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))
    return service


def calendar_insertion(service):
    calendar = {
        'summary': 'Your NBA team(s) Schedule',
        'timeZone': 'America/Los_Angeles'
    }

    created_calendar = service.calendars().insert(body=calendar).execute()

    print(created_calendar['id'])


def event_insertion(service, event):
    calendar_list_entry = service.calendarList().get(calendarId='primary').execute()
    if calendar_list_entry['accessRole']:
        event = {
            'summary': "test",
            'location': 'gg',
            'description': 'gg',
            'start': {
                'dateTime': '2020-02-18T09:00:00-07:00',
                'timeZone': 'America/New_York',
            },
            'end': {
                'dateTime': '2020-02-19T09:00:00-07:00',
                'timeZone': 'America/New_York',
            },
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
        print(f"The event has been created! View it at {event.get('htmlLink')}!")

calendar_insertion(calendar_connection())
