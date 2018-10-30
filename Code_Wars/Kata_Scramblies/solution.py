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

def scramble2(s1, s2):
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

def scramble(s1, s2):
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))

    counter1 = 0;
    counter2 = 0

    while counter2 < len(s2):
        letter2 = s2[counter2]
        letter1 = s1[counter1]

        # they dont match, let's see if we can increment counter1
        if letter2 != letter1:
            while s1[counter1] < letter2:
                counter1 += 1;
            if letter2 != s1[counter1]:
                return False

        counter2 += 1
        counter1 += 1

    return True

print(scramble('rkqodlw', 'world')) #true
print(scramble('cedewaraaossoqqyt', 'codewars')) #true
print(scramble('katas', 'stea'))#false
print(scramble('scriptjava', 'javascript')) #true
print(scramble('scriptingjava', 'javascript')) #true


class Tests(unittest.TestCase):
    def test_all(self):
        self.assertTrue(scramble('rkqodlw', 'world'))
        self.assertTrue(scramble('cedewaraaossoqqyt', 'codewars'))
        self.assertFalse(scramble('katas', 'stea'))
        self.assertTrue(scramble('scriptjava', 'javascript'))
        self.assertTrue(scramble('scriptingjava', 'javascript'))
        self.assertTrue(scramble('fxjnacpzav', 'xjzaavnpcf'))
unittest.main

