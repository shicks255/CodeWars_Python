# !python3

from unittest import TestCase

def next_bigger(n):
    numbers = list(str(n))

    i = len(numbers)-1
    temp = numbers[i]
    numbers[i] = numbers[i-1]
    numbers[i-1] = temp
    if numbers <= list(str(n)):
        i = len(numbers)-2
        temp = numbers[i]
        numbers[i] = numbers[i-1]
        numbers[i-1] = temp
        return int(''.join(numbers[:i]) + ''.join(sorted(numbers[i:])))
    return int(''.join(numbers))


next_bigger(2074)

class Tests(TestCase):
    def testAll(self):
        # self.assertEqual(next_bigger(12),21)
        # self.assertEqual(next_bigger(513),531)
        # self.assertEqual(next_bigger(2017),2071)
        # self.assertEqual(next_bigger(414),441)
        # self.assertEqual(next_bigger(144),414)
        self.assertEqual(next_bigger(1234567890),1234567908)
        # self.assertEqual(next_bigger(2074),2407)
        # self.assertEqual(next_bigger(1047),1074)