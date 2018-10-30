# !python3

# https://www.codewars.com/kata/scramblies

# Complete the function scramble(str1, str2) that returns true
# if a portion of str1 characters can be rearranged to match str2, otherwise returns false.
#
# Notes:
#
# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered
# Examples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False

import unittest

def scramble(s1, s2):



scramble('rkqodlw', 'world') #true
scramble('cedewaraaossoqqyt', 'codewars') #true
scramble('katas', 'stea') #false
scramble('scriptjava', 'javascript') #true
scramble('scriptingjava', 'javascript') #true


class Tests(unittest.TestCase):
    def test_all(self):
        self.assertTrue(scramble('rkqodlw', 'world'))
        self.assertTrue(scramble('cedewaraaossoqqyt', 'codewars'))
        self.assertFalse(scramble('katas', 'stea'))
        self.assertTrue(scramble('scriptjava', 'javascript'))
        self.assertTrue(scramble('scriptingjava', 'javascript'))
unittest.main

