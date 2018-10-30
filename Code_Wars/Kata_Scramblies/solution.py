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

def mapping(x, wordMap):
    if x in wordMap:
        wordMap[x] = wordMap[x] + 1
    else:
        wordMap[x] = 1

def scramble(s1, s2):
    firstWordCharMap = {}
    for let in s1:
        mapping(let, firstWordCharMap)
    secondWordCharMap = {}
    for let in s2:
        mapping(let, secondWordCharMap)

    for key in secondWordCharMap.keys():
        if key not in firstWordCharMap:
            return False
        if secondWordCharMap[key] > firstWordCharMap[key]:
            return False

    return True

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
        self.assertTrue(scramble('fxjnacpzav', 'xjzaavnpcf'))
unittest.main

