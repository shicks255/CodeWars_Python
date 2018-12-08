
import sys
import os

os.chdir(sys.path[0])

def findPath(y, x, coords):
    x2 = int(coords[0:coords.index(',')])
    y2 = int(coords[coords.index(',')+1:])

    xDist = abs(x - x2)
    yDist = abs(y - y2)
    return xDist + yDist

def isInfinite(x, y, grid):
    thisValue = grid[y][x]

    tempx = x
    tempy = y-1
    tempThisValue = thisValue

    while tempy > 0:
        if grid[tempy][tempx] != grid[y][x].replace('*',''):
            break
        tempy -= 1
    if tempy <= 0:
        return False
    else:
        tempy = y+1

    while tempy != len(grid):
        if grid[tempy][tempx] != grid[y][x].replace('*',''):
            break
        tempy += 1
    if tempy == len(grid):
        return False
    else:
        tempy = y
        tempx = x-1


    while tempx > 0:
        if grid[tempy][tempx] != grid[y][x].replace('*', ''):
            break
        tempx -= 1
    if tempx <= 0:
        return False
    else:
        tempx = x + 1

    while tempx < len(grid[y]):
        if grid[tempy][tempx] != grid[y][x].replace('*',''):
            break
        if tempx == len(grid[y]):
            return False
        else:
            return True

def getUsableArea(x, y, grid):
    value = grid[int(y)][int(x)].replace('*', '')
    counter = 0
    for yy, row in enumerate(grid):
        for xx in grid[yy]:
            thisValue = grid[int(yy)][int(xx)]
            if '.' in thisValue:
                continue
            if '*' in thisValue:
                continue
            if thisValue == value:
                counter += 1
    return counter

with open('input.txt') as input:
    coords = [x.rstrip('\n') for x in input.readlines()]
    xCoords = [int(y[0:y.index(',')]) for y in coords]
    yCoords = [int(x[x.index(',')+1:]) for x in coords]

    largestX = max(xCoords) +1
    largestY = max(yCoords) +1

    grid = [['.' for _ in range(largestX)] for _ in range(largestY)]
    # setting up grid coordinates
    for i,coord in enumerate(coords):
        x = int(coord[0:coord.index(',')])
        y = int(coord[coord.index(',')+1:])
        grid[y][x] = '*' + str(i+1) + '*'

    for y in range(largestY):
        for x in range(largestX):
            bestDistance = None
            bestCoord = None
            if '*' in grid[y][x]:
                continue
            for i, coord in enumerate(coords):
                distance = findPath(y, x, coord)
                if bestDistance is None:
                    bestDistance = distance
                    bestCoord = i+1
                    continue
                if distance == bestDistance:
                    bestCoord = '.'
                    break
                if distance < bestDistance:
                    bestDistance = distance
                    bestCoord = i+1

            grid[y][x] = str(bestCoord)
            # print(bestCoord)

    # print(grid)
    # pprint(grid)

    print('\n'.join(['\t\t'.join([cell for cell in row]) for row in grid]))

    possibleCoords = [x for x in coords if isInfinite(int(x[0:x.index(',')]), int(x[x.index(',')+1:]), grid)]
    print(possibleCoords)

    counter = 0
    for p in possibleCoords:
        count = getUsableArea(p[0:p.index(',')], p[p.index(',')+1:], grid)
        if count > counter:
            counter = count

    print(counter)
