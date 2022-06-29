from unittest import TestCase

from src import alerter


class TestAlerter(TestCase):

    def test_alerter(self):
        alerter.alert_in_celcius(300.6)
        alerter.alert_in_celcius(445.8)
        alerter.alert_in_celcius(45)
        self.assertEqual(alerter.alert_failure_count, 1)
