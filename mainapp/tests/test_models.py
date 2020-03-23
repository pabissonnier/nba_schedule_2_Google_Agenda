from django.test import TestCase
from mainapp.models import Schedule


class ScheduleTestCase(TestCase):

    def setUp(self):
        Schedule.objects.create(date="2019-11-10", hour="20:00", vteam='Brooklyn Nets',
                               hteam='Phoenix Suns', arena='Talking Stick Resort Arena')
        Schedule.objects.create(date="2019-11-10", hour="21:00", vteam='Atlanta Hawks',
                                hteam='Portland Trail Blazers', arena='Moda Center')
        Schedule.objects.create(date="2019-11-10", hour="21:30", vteam='Toronto Raptors',
                                hteam='Los Angeles Lakers', arena='Staples Center')
        Schedule.objects.create(date="2019-11-11", hour="19:00", vteam='Minnesota Timberwolves',
                                hteam='Brooklyn Nets', arena='Little Caesars Arena')
        Schedule.objects.create(date="2019-11-11", hour="19:30", vteam='Dallas Mavericks',
                                hteam='Boston Celtics', arena='TD Garden')
        Schedule.objects.create(date="2019-11-12", hour="19:30", vteam='Memphis Grizzlies',
                                hteam='San Antonio Spurs', arena='AT&T Center')
        Schedule.objects.create(date="2019-11-12", hour="20:00", vteam='Los Angeles Lakers',
                                hteam='Toronto Raptors', arena='Smoothie King Center')
        Schedule.objects.create(date="2019-11-13", hour="22:30", vteam='Utah Jazz',
                                hteam='Golden State Warriors', arena='Chase Center')
        Schedule.objects.create(date="2019-11-13", hour="22:30", vteam='Toronto Raptors',
                                hteam='LA Clippers', arena='Staples Center')
        Schedule.objects.create(date="2019-11-14", hour="19:00", vteam='Oklahoma City Thunder',
                                hteam='Indiana Pacers', arena='Bankers Life Fieldhouse')
        Schedule.objects.create(date="2019-11-15", hour="19:00", vteam='Cleveland Cavaliers ',
                                hteam='Philadelphia 76ers', arena='Wells Fargo Center')

    def test_extraction_to_gformat(self):
        game = Schedule.objects.get(id=1)
        result = {'summary': 'Brooklyn Nets @ Phoenix Suns', 'location': 'Talking Stick Resort Arena',
                  'description': "Your NBA game between Brooklyn Nets and Phoenix Suns starting on the "
                                 "2019-11-10 at 20:00 EST",
                  'start': {'dateTime': "2019-11-10T20:00:00", 'timeZone': "America/New_York"},
                  'end': {'dateTime': "2019-11-10T21:00:00", 'timeZone': "America/New_York"}}
        function_output = Schedule.extraction_to_gformat(Schedule(), game)
        self.assertEqual(function_output, result)


