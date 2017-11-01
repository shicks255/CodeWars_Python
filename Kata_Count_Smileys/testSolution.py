#! python3


import unittest
from solution import count_smileys


class Tests(unittest.TestCase):
    def test_all(self):
        print(count_smileys([':)', ';(', ';}', ':-D']))
        self.assertEquals(count_smileys([':)', ';(', ';}', ':-D']) == 26)
