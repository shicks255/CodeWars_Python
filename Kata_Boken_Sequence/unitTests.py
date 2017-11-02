# ! python3

import unittest
from solution import find_missing_number


class Tests(unittest.TestCase):
    def test_all(self):
        self.assertEqual(find_missing_number("1 3 2 5"), 4)  # returns 4, because 4 is missing
        self.assertEqual(find_missing_number("1 2 3 4"), 0)  # returns 0, because the sequence isn't broken
        self.assertEqual(find_missing_number("1 5"), 2)  # returns 2, because the sequence is missing more than one number and 2 is lowest
        self.assertEqual(find_missing_number("2 1 4 3 a"), 1)  # returns 1, because it's an invalid sequence. ind this case, it's invalid because contain a non numerical character


if __name__ == '__main__':
    unittest.main()