from django.test import TestCase
from weather.weather import Weather
from unittest.mock import Mock, patch

class Test_weather(TestCase):

    def setUp(self):
        self.data = {
            "data": [
                {"temperature": 4},
                {"temperature": 6},
                {"temperature": 8},
            ]
        }

    @patch("requests.post")
    def test_max_temp(self, mocked_requests):
        mocked_requests.return_value.json = Mock(return_value = self.data)

        result = Weather.max_temp()

        self.assertEqual(result, 8)

    @patch("requests.post")
    def test_min_temp(self, mocked_requests):
        mocked_requests.return_value.json = Mock(return_value = self.data)

        result = Weather.min_temp()

        self.assertEqual(result, 4)

    @patch("requests.post")
    def test_avg_temp(self, mocked_requests):
        mocked_requests.return_value.json = Mock(return_value = self.data)

        result = Weather.avg_temp()

        self.assertEqual(result, 6)


