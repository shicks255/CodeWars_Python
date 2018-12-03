
import os
import sys
import re

os.chdir(sys.path[0])

def parseInput(input):
    regex = re.compile('\d*,\d*')
    matchObj = regex.search(input)
    if matchObj:
        groups = str(matchObj.group())
        regex2 = re.compile('\d*x\d*')
        matchObj2 = regex2.search(input)
        if matchObj2:
            groups2 = str(matchObj2.group())
            indexOfComma = groups.index(',')
            fromLeft = groups[0:indexOfComma]
            fromTop = groups[indexOfComma+1:]
            indexOfX = groups2.index('x')
            width = groups2[0:indexOfX]
            height = groups2[indexOfX+1:]
            return [fromLeft, fromTop, width, height]

with open("input.txt") as input:
    lines = [x.rstrip('\n') for x in input.readlines()]
    for line in lines:
        print(parseInput(line))

