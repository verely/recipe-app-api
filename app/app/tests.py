"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):

    def test_add_numbers(self):

        res = calc.add(3, 4)

        self.assertEqual(res, 7)
