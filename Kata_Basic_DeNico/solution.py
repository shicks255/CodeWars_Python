# !python 3
# Task
#
# Write a function deNico/de_nico() that accepts two parameters:
#
# key/$key - string consists of unique letters and digits
# message/$message - string with encoded message
# and decodes the message using the key.
#
# First create a numeric key basing on the provided key by assigning each
# letter position in which it is located after setting the letters from key in an alphabetical order.
#
# For example, for the key crazy we will get 23154 because of acryz (sorted letters from the key).
# Let's decode cseerntiofarmit on using our crazy key.

# 1 2 3 4 5
# ---------
# c s e e r
# n t i o f
# a r m i t
#   o n
#
# 2 3 1 5 4
# ---------
# s e c r e
# t i n f o
# r m a t i
# o n

import unittest

def de_nico(key,msg):
    keyToNumberMap = {}

    keyAsList = list(key)
    keyAsList.sort()
    int = 1
    for letter in keyAsList:
        keyToNumberMap[letter] = int
        int += 1

    newKey = []
    for letter in key:
        newKey.append(keyToNumberMap[letter])

    keyLength = len(key)
    listOf5LengthChunks = [msg[i: i + keyLength] for i in range(0, len(msg), keyLength)]

    newMessage = ""

    for chunk in listOf5LengthChunks:
        for int in newKey:
            if len(chunk) >= int:
                newMessage += chunk[int-1]

    return newMessage.strip()

print(de_nico("crazy", "cseerntiofarmit on  "))

# class Tests(unittest.TestCase):
#     def test_all(self):
#         test.describe("Basic tests")
#         self.assertEquals(de_nico("crazy", "cseerntiofarmit on  "), "secretinformation")
        # self.assertEquals(de_nico("crazy", "cseerntiofarmit on"), "secretinformation")
        # self.assertEquals(de_nico("abc", "abcd"), "abcd")
        # self.assertEquals(de_nico("ba", "2143658709"), "1234567890")
        # self.assertEquals(de_nico("a", "message"), "message")
        # self.assertEquals(de_nico("key", "eky"), "key")
#
#
# unittest.main()
