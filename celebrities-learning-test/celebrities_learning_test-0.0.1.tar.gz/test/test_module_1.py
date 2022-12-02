import unittest
from celebrities_births import Date

class DateTest(unittest.TestCase):
    
    def setUp(self):
        self.new_date = Date(32, 10, 2021)

    def test_date_valid(self):
        self.assertRaises(ValueError)

    def test___day_of_month_valid(self):
        self.assertEqual(len(self._day_of_month), 31)

    def test___month_str_valid(self):
        self.assertEqual(len(self.__month_str), 12)


t=(1)
