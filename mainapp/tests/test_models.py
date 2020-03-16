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
                                hteam='Detroit Pistons', arena='Little Caesars Arena')
        Schedule.objects.create(date="2019-11-11", hour="19:30", vteam='Dallas Mavericks',
                                hteam='Boston Celtics', arena='TD Garden')
        Schedule.objects.create(date="2019-11-11", hour="19:30", vteam='Memphis Grizzlies',
                                hteam='San Antonio Spurs', arena='AT&T Center')
        Schedule.objects.create(date="2019-11-11", hour="20:00", vteam='Houston Rockets',
                                hteam='New Orleans Pelicans', arena='Smoothie King Center')
        Schedule.objects.create(date="2019-11-11", hour="22:30", vteam='Utah Jazz',
                                hteam='Golden State Warriors', arena='Chase Center')
        Schedule.objects.create(date="2019-11-11", hour="22:30", vteam='Toronto Raptors',
                                hteam='LA Clippers', arena='Staples Center')
        Schedule.objects.create(date="2019-11-12", hour="19:00", vteam='Oklahoma City Thunder',
                                hteam='Indiana Pacers', arena='Bankers Life Fieldhouse')
        Schedule.objects.create(date="2019-11-12", hour="19:00", vteam='Cleveland Cavaliers ',
                                hteam='Philadelphia 76ers', arena='Wells Fargo Center')

    def test_get_team_agenda(self):
        team_list = ['Brooklyn Nets', 'Los Angeles Lakers', 'Toronto Raptors']
        function_output = Schedule.get_teams_agenda(Schedule(), team_list)
        self.assertEqual()
        # find query set result

    


    def test_find_similar_name(self):
        query = "lait chocolat"
        result = ['Gâteau au chocolat noir', 'Chocolat Lait', 'Chocolat Lait', 'Bâtonnets de chocolat',
                  'Croustifondante Chocolat',
                  'Ferme & Fondant Chocolat', 'Delichoc', 'Délichoc sablé', 'Savane Le Classique Chocolat',
                  'Biscuits nappés chocolat noir', 'BN goût chocolat', 'Biscuit Avoine et Chocolat',
                  'Fitness Chocolat Noir', 'Kinder chocolat mini eggs', 'Chocolat Happy', 'Kinder Chocolat',
                  'Bitter Schokolade', 'Petit-beurre Chocolat Noir', 'Biscuit choco fondant noir']
        function_output = Product.find_similar_name(Product(), query)
        self.assertEqual(function_output, result)

    def test_product_chosen(self):
        query = "bâtonnets Sablés Chocolat Au Lait"

        name = "Bâtonnets sablés chocolat au lait"
        picture = 'https://static.openfoodfacts.org/images/products/335/003/311/1868/front_fr.27.400.jpg'
        nutriscore = 'e'
        category = 'Snacks'
        link = 'https://fr.openfoodfacts.org/produit/3350033111868/batonnets-sables-chocolat-au-lait-monoprix-gourmet'
        id = 1295
        result = name, picture, nutriscore, category, link, id

        function_output = Product.product_chosen(Product(), query)
        self.assertEqual(function_output, result)

    def test_product_chosen_sim(self):
        query = 1295

        name = "Bâtonnets sablés chocolat au lait"
        picture = 'https://static.openfoodfacts.org/images/products/335/003/311/1868/front_fr.27.400.jpg'
        nutriscore = 'e'
        category = 'Snacks'
        link = 'https://fr.openfoodfacts.org/produit/3350033111868/batonnets-sables-chocolat-au-lait-monoprix-gourmet'
        id = 1295
        result = name, picture, nutriscore, category, link, id

        function_output = Product.product_chosen_sim(Product(), query)
        self.assertEqual(function_output, result)
