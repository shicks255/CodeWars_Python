# !python3

# Define a function isPrime that takes one integer argument
# and returns true or false depending on if the integer is a prime.
#
# Per Wikipedia, a prime number (or a prime) is a natural number g
# reater than 1 that has no positive divisors other than 1 and itself.

import unittest

def is_prime(num):
    matchesFound = 0
    x = 1
    while x <= num:
        y = 1
        while y < num:
            if y * x == num:
                matchesFound += 1
            y += 1
        x += 1

    if matchesFound > 0:
        primeNumber = False
    if matchesFound == 0:
        primeNumber = True

    if num == 1 or num == -1:
        primeNumber = False

    return primeNumber

is_prime(0)
