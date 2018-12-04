
import os
import sys
import re

os.chdir(sys.path[0])

# to give back a tuple with [fromLeft, fromTop, width, height, id]
def parseInput(input):
    regexId = re.compile('#\d*')
    matchId = regexId.search(input)
    if matchId:
        id = str(matchId.group())
        id = id.replace('#','')
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
                return [fromLeft, fromTop, width, height, id]

with open("input.txt") as input:
    lines = [parseInput(x.rstrip('\n')) for x in input.readlines()]
    widths = [int(x[0]) + int(x[2]) for x in lines]
    heights = [int(x[1]) + int(x[3]) for x in lines]
    maxWidth = max(widths)
    maxHeight = max(heights)

    grid = [[0 for x in range(maxHeight)] for j in range(maxWidth)]

    for line in lines:
        fromLeft = line[0]
        fromTop  = line[1]
        width = line[2]
        height = line[3]
        for x in range(width):
            for y in range(height):
                grid[fromLeft + x][fromTop + y] += 1

    squareCounter = 0
    for x in range(maxWidth):
        for y in range(maxHeight):
            if grid[x][y] > 1:
                squareCounter += 1
    print(squareCounter)

#     part 2
    for line in lines:
        fromLeft = line[0]
        fromTop = line[1]
        width = line[2]
        height = line[3]
        id = line[4]
        good = True;
        for x in range(width):
            for y in range(height):
                if grid[fromLeft + x][fromTop + y] > 1:
                    good = False
        if good:
            print(id)



