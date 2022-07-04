from unittest import TestCase

from src import alerter


class TestAlerter(TestCase):

    def test_alerter(self):
        alerter.alert_in_celcius(300.6)
        self.assertEqual(alerter.alert_failure_count, 1)
        alerter.alert_in_celcius(445.8)
        self.assertEqual(alerter.alert_failure_count, 2)
        alerter.alert_in_celcius(56.8)
        self.assertEqual(alerter.alert_failure_count, 2)

