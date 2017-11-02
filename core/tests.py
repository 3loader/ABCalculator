from urllib.parse import urlencode

from django.test import TestCase


class CalculatorTests(TestCase):

    def test_home_page(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_calculator(self):
        get_params = {
            'control_visitors': 2000,
            'variation_visitors': 3000,
            'control_conversions': 134,
            'variation_conversions': 165,
        }

        data = self.client.get('/calculate/?{0}'.format(urlencode(get_params)))
        resp = data.json()

        self.assertTrue(resp['significance'] == 'Yes!')
        self.assertTrue(resp['p_value'] == 0.043)
