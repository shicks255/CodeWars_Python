
import os
import sys
from collections import Counter

os.chdir(sys.path[0])

def needToRemove(x, y):
    if x.istitle():
        return y.istitle() == False
    if x.istitle() == False:
        return y.istitle()

with open('input.txt') as input:
    line = input.read()
    charList = [x for x in line]
    start = 0
    while start < len(charList)-2:
        x = charList[start]
        y = charList[start+1]
        if x.upper() == y.upper():
            if needToRemove(str(x), str(y)):
                # print('removing ' + x + ' '  + y)
                del charList[start:start+2]
                start -= 2
                if start < 0:
                    start = 0
                    continue
        start += 1

    # print(charList)
    # print(len(charList))

    # part 2
    charListNew = [x.upper() for x in line]
    counter = Counter(charListNew)
    print(counter)
    mostCommon = ['',0]
    for item, value in counter.items():
        if value > mostCommon[1]:
            mostCommon[0] = item
            mostCommon[1] = value

    someList = [x for x in line if x.upper() != mostCommon[0]]

    start = 0
    while start < len(someList)-2:
        x = someList[start]
        y = someList[start+1]
        if x.upper() == y.upper():
            if needToRemove(str(x), str(y)):
            # print('removing ' + x + ' '  + y)
                del someList[start:start+2]
                start -= 2
            if start < 0:
                start = 0
                continue
        start += 1

    print(someList)
    print(len(someList))
    print(counter)
