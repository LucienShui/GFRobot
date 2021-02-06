import unittest
from main import check
from datetime import datetime


class GanFanTestCase(unittest.TestCase):
    def test_check(self):
        test_case: list = [
            ['2021-02-04 22:55:00', True],
            ['2021-02-05 11:55:00', True],
            ['2021-02-05 20:55:00', True],
            ['2021-02-05 22:55:00', False],
            ['2021-02-06 22:55:00', False],
        ]

        for str_datetime, label in test_case:
            now = datetime.strptime(str_datetime, '%Y-%m-%d %H:%M:%S')
            self.assertEqual(label, check(now))


if __name__ == '__main__':
    unittest.main()
