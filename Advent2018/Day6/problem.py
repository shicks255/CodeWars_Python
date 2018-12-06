
import sys
import os

os.chdir(sys.path[0])

with open('input.txt') as input:
    coords = [x.rstrip('\n') for x in input.readlines()]
    xCoords = [int(x[0:x.index(',')]) for x in coords]
    yCoords = [int(y[y.index(',')+1:]) for y in coords]

    largestX = max(xCoords)
    largestY = max(yCoords)

    grid = [0 for _ in range(largestY) for _ in range(largestX)]

    print(grid)
