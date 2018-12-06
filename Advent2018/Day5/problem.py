
import os
import sys

os.chdir(sys.path[0])

def printSizeAfterPolymers(list):
    start = 0
    while start < len(list)-2:
        x = list[start]
        y = list[start+1]
        if x.upper() == y.upper():
            if needToRemove(str(x), str(y)):
                del list[start:start+2]
                start -= 2
                if start < 0:
                    start = 0
                    continue
        start += 1
    return len(list)

def needToRemove(x, y):
    if x.istitle():
        return y.istitle() == False
    if x.istitle() == False:
        return y.istitle()

with open('input.txt') as input:
    line = input.read()
    charList = [x for x in line]
    # part 1
    print(printSizeAfterPolymers(charList))

    # part 2
    charListNew = [x.upper() for x in line]
    letters = ['A', 'B', 'C', 'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    bestLength = 50000

    for letter in letters:
        letterList = [x for x in line if x.upper() != letter]
        length = printSizeAfterPolymers(letterList)
        print(length)
        if length < bestLength:
            bestLength = length

    print(bestLength)

