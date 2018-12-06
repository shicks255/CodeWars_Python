
import os
import sys

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

    print(charList)
    print(len(charList))