#! python3


import unittest
from solution import count_smileys


class Tests(unittest.TestCase):
    def test_all(self):
        self.assertEqual(count_smileys([':)', ';(', ';}', ':-D']), 2)
        self.assertEqual(count_smileys([';D', ':-(', ':-)', ';~)']), 3)
        self.assertEqual(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)

if __name__ == '__main__':
    unittest.main()
