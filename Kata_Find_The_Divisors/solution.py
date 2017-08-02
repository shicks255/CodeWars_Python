# !python3

# Create a function named divisors that takes an integer and returns an array
# with all of the integer's divisors(except for 1 and the number itself).
# If the number is prime return the string '(integer) is prime'
# (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
#
# Example:
#
# divisors(12); #should return [2,3,4,6]
# divisors(25); #should return [5]
# divisors(13); #should return "13 is prime"

import unittest

def divisors(integer):
    divisorResults = []

    for i in range(integer):
        if i == 1 or i == 0:
            continue
        if i == integer:
            continue

        if integer % i == 0:
            divisorResults.append(i)

    if len(divisorResults) == 0:
        return str(integer) + " is prime"
    else:
        return divisorResults

print(divisors(15))


class Tests(unittest.TestCase):
    def test_all(self):
        # test.describe("Basic tests")
        self.assertEquals(divisors(15), [3, 5])
        self.assertEquals(divisors(12), [2, 3, 4, 6])
        self.assertEquals(divisors(13), "13 is prime")
        self.assertEquals(divisors(20), [2, 4, 5, 10])
unittest.main()