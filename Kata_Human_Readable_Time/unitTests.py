# python! 3



import unittest
from .solution import


class Tests(unittest.TestCase):
    def test_all(self):
        self.assert_equal(make_readable(0), "00:00:00")
        self.assert_equal(make_readable(5), "00:00:05")
        self.assert_equal(make_readable(60), "00:01:00")
        self.assert_equal(make_readable(86399), "23:59:59")
        self.assert_equal(make_readable(359999), "99:59:59")


if __main__ == '__main__':
    unittest.main()



