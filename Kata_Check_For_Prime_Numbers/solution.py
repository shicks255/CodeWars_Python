# !python3

# In this kata you will create a function to check a non-negative input to see if it is a prime number.
#
# The function will take in a number and will return True if it is a prime number and False if it is not.
#
# A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
import unittest

def is_prime(n):
    matchesFound = 0
    x = 1
    while x < n:
        y = 1
        while y < n:
            if y * x == n:
                matchesFound += 1
            y += 1
        x += 1

    if matchesFound > 0:
        primeNumber = False
    if matchesFound == 0:
        primeNumber = True

    if n == 0 or n == 1:
        primeNumber = False

    return primeNumber

is_prime(11)
