# python! 3
import unittest
from solution import make_readable


class Tests(unittest.TestCase):
    def test_all(self):
        self.assertEqual(make_readable(0), "00:00:00")
        self.assertEqual(make_readable(5), "00:00:05")
        self.assertEqual(make_readable(60), "00:01:00")
        self.assertEqual(make_readable(86399), "23:59:59")
        self.assertEqual(make_readable(359999), "99:59:59")


if __name__ == '__main__':
    unittest.main()



