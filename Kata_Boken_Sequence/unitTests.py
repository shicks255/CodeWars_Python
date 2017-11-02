#! python3

import unittest
from Kata_Boken_Sequence.solution import find_missing_number


class Tests(unittest.TestCase):
    def test_all(self):
            # returns 4, because 4 is missing
        self.assertEqual(find_missing_number("1 3 2 5"), 4)

            # returns 0, because the sequence isn't broken
        self.assertEqual(find_missing_number("1 2 3 4"), 0)

        #     returns 2, because the sequence is missing more than one number and 2 is lowest
        self.assertEqual(find_missing_number("1 5"), 2)

        #     returns 1, because it's an invalid sequence. ind this case, it's invalid because contain a non numerical character
        self.assertEqual(find_missing_number("2 1 4 3 a"), 1)

        self.assertEqual(find_missing_number("1 2 3 5"), 4, "It must work for missing middle terms")
        self.assertEqual(find_missing_number("1 5"), 2, "It must work for missing more than one element")
        self.assertEqual(find_missing_number(""), 0, "It must return 0 for an empty sequence")
        self.assertEqual(find_missing_number("1 2 3 4 5"), 0, "It must return 0 if no number is missing")
        self.assertEqual(find_missing_number("2 3 4 5"), 1, "It must return 1 for a sequence missing the first element")
        self.assertEqual(find_missing_number("2 6 4 5 3"), 1, "It must work for a shuffled input")
        self.assertEqual(find_missing_number("2 1 4 3 a"), 1, "It must return 1 for an invalid sequence")
        self.assertEqual(find_missing_number("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 51 52"), 50, "It must return 1 for an invalid sequence")


if __name__ == '__main__':
    unittest.main()
