
import sys
import os
from pprint import pprint

os.chdir(sys.path[0])

def findPath(x, y, coords):
    x2 = int(coords[0:coords.index(',')])
    y2 = int(coords[coords.index(',')+1:])

    xDist = abs(x - x2)
    yDist = abs(y - y2)
    return xDist + yDist


with open('input.txt') as input:
    coords = [x.rstrip('\n') for x in input.readlines()]
    xCoords = [int(x[0:x.index(',')]) for x in coords]
    yCoords = [int(y[y.index(',')+1:]) for y in coords]

    largestX = max(xCoords)+1
    largestY = max(yCoords)+1

    grid = [['.' for _ in range(largestY)] for _ in range(largestX)]
    # setting up grid coordinates
    for i,coord in enumerate(coords):
        x = int(coord[0:coord.index(',')])
        y = int(coord[coord.index(',')+1:])
        grid[x][y] = '*' + str(i+1) + '*'

    for x in range(largestX):
        for y in range(largestY):
            bestDistance = None
            bestCoord = None
            if '*' in grid[x][y]:
                continue
            for i, coord in enumerate(coords):
                distance = findPath(x, y, coord)
                if bestDistance is None:
                    bestDistance = distance
                    continue
                if distance == bestDistance:
                    bestCoord = '.'
                    break
                if distance < bestDistance:
                    bestDistance = distance
                    bestCoord = i


            # grid[x][y] = bestCoord
            # print(bestCoord)

    # print(grid)
    # pprint(grid)

    print('\n'.join(['\t'.join([cell for cell in row]) for row in grid]))
