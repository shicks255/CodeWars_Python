# !python3

from unittest import TestCase

def next_bigger(n):
    numbers = str(n)

    i = len(numbers)-2
    last = numbers[i+1]
    while i >= 0:
        next = numbers[i]
        if last < next:
            numbers[i] = next
            numbers[i-1] = last
            return int(numbers)

        i -= 1



next_bigger(123)

# class Tests(TestCase):
#     def testAll(self):
        # self.assert_equals(next_bigger(12),21)
        # self.assert_equals(next_bigger(513),531)
        # self.assert_equals(next_bigger(2017),2071)
        # self.assert_equals(next_bigger(414),441)
        # self.assert_equals(next_bigger(144),414)
        # self.assert_equals(next_bigger(2074),2407)
        # self.assert_equals(next_bigger(1047),1074)