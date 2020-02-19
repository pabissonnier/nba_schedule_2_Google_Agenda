from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from datetime import datetime

game_list = [{'summary': 'Indiana Pacers @ Denver Nuggets', 'location': 'Stadium', 'description': 'Your schedule from NS2GC', 'start': {'dateTime': '2020-01-19T20:00:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2020-01-19T23:00:00', 'timeZone': 'America/New_York'}},
{'summary': 'Houston Rockets @ Denver Nuggets', 'location': 'Stadium', 'description': 'Your schedule from NS2GC', 'start': {'dateTime': '2020-01-26T15:30:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2020-01-26T18:30:00', 'timeZone': 'America/New_York'}},
{'summary': 'Utah Jazz @ Denver Nuggets', 'location': 'Stadium', 'description': 'Your schedule from NS2GC', 'start': {'dateTime': '2020-01-30T22:30:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2020-01-30T01:30:00', 'timeZone': 'America/New_York'}},
{'summary': 'Portland Trail Blazers @ Denver Nuggets', 'location': 'Stadium', 'description': 'Your schedule from NS2GC', 'start': {'dateTime': '2020-02-04T22:00:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2020-02-04T01:00:00', 'timeZone': 'America/New_York'}},
{'summary': 'San Antonio Spurs @ Denver Nuggets', 'location': 'Stadium', 'description': 'Your schedule from NS2GC', 'start': {'dateTime': '2020-02-10T21:00:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2020-02-10T00:00:00', 'timeZone': 'America/New_York'}},
{'summary': 'Los Angeles Lakers @ Denver Nuggets', 'location': 'Stadium', 'description': 'Your schedule from NS2GC', 'start': {'dateTime': '2020-02-12T22:00:00', 'timeZone': 'America/New_York'}, 'end': {'dateTime': '2020-02-12T01:00:00', 'timeZone': 'America/New_York'}}]


def calendar_connection():
    SCOPES = "https://www.googleapis.com/auth/calendar"
    store = file.Storage('mainapp/token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('mainapp/credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))
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


