from unittest import TestCase

import src.aligned_color_map as a


class TestAlignedColorMap(TestCase):

    def test_print_color_map(self):
        self.assertEqual(a.print_color_map(), 25)
        self.assertEqual(a.color_map[0].find("|"), a.color_map[24].find("|"))
