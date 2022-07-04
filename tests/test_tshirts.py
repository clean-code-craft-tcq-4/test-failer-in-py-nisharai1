from unittest import TestCase
from src import tshirts


class TestTshirts(TestCase):

    def test_tshirts_size(self):
        self.assertEqual(tshirts.size(37), 'S')
        self.assertEqual(tshirts.size(38), 'S')
        self.assertEqual(tshirts.size(47), 'L')
        self.assertEqual(tshirts.size(40), 'M')
        self.assertEqual(tshirts.size(5), None)
        self.assertEqual(tshirts.size(-5), None)
        self.assertEqual(tshirts.size(55), None)
