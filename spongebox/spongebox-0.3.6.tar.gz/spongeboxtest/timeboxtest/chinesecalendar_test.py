import unittest
from spongebox.timebox import ChineseCalendar


class MyTestCase(unittest.TestCase):
    def test_something(self):
        cc = ChineseCalendar("2022-01-01")
        self.assertEqual(4, cc.count_WDAY('2022-10-01', '2022-10-11'))

    def test1_something(self):
        cc = ChineseCalendar("2022-01-01")
        self.assertEqual("2022-10-11", cc.move_WDAY('2022-10-01', 4))

    def test2_something(self):
        cc = ChineseCalendar("2022-01-01")
        self.assertEqual("2022-10-09", cc.move_WDAY('2022-10-08', 2))  # add assertion here


if __name__ == '__main__':
    unittest.main()
