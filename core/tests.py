from urllib.parse import urlencode

from django.test import TestCase


class CalculatorTests(TestCase):

    def test_home_page(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_calculator_with_normal_params(self):
        params = {
            'control_visitors': 2000,
            'variation_visitors': 3000,
            'control_conversions': 134,
            'variation_conversions': 165,
        }

        data = self.client.get('/calculate/?{0}'.format(urlencode(params)))
        resp = data.json()

        self.assertTrue(resp['significance'] == 'Yes!')
        self.assertTrue(resp['p_value'] == 0.043)

    def test_calculator_without_params(self):
        data = self.client.get('/calculate/')
        resp = data.json()

        self.assertTrue(resp['significance'] == 'No')
        self.assertTrue(resp['p_value'] == 'NaN')

    def test_calculator_with_bad_params(self):
        params = {
            'control_visitors': 1,
            'variation_visitors': 25,
            'control_conversions': 1000,
            'variation_conversions': -5,
        }

        data = self.client.get('/calculate/?{0}'.format(urlencode(params)))
        resp = data.json()

        self.assertTrue(resp['significance'] == 'No')
        self.assertTrue(resp['p_value'] == 'NaN')
