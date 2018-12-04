
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
            fromLeft = int(groups[0:indexOfComma])
            fromTop = int(groups[indexOfComma+1:])
            indexOfX = int(groups2.index('x'))
            width = int(groups2[0:indexOfX])
            height = int(groups2[indexOfX+1:])
            return [fromLeft, fromTop, width, height]

with open("input.txt") as input:
    lines = [x.rstrip('\n') for x in input.readlines()]
    lines2 = [parseInput(x) for x in lines]
    widths = [int(x[0]) + int(x[2]) for x in lines2]
    heights = [int(x[1]) + int(x[3]) for x in lines2]
    maxWidth = max(widths)
    maxHeight = max(heights)

    grid = [[0 for x in range(maxHeight)] for j in range(maxWidth)]

    for line in lines2:
        fromLeft = line[0]
        fromTop  = line[1]
        width = line[2]
        height = line[3]
        for x in range(width):
            for y in range(height):
                grid[fromLeft + x][fromTop + y] += 1

    print(grid)

    squareCounter = 0
    for x in range(maxWidth):
        for y in range(maxHeight):
            if grid[x][y] > 1:
                squareCounter += 1
    print(squareCounter)



