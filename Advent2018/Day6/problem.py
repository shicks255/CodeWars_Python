
import sys
import os

os.chdir(sys.path[0])

def findClosest(x, y, grid, steps, checkedList):
    if (x >= len(grid) or x < 0):
        return None
    if (y >= len(grid[x]) or x < 0):
        return None

    point = grid[x][y]
    if point != '.':
        return [point[:1], steps]

    checkedList.append([x,y])

    if [x-1,y] not in checkedList:
        left = findClosest(x-1, y, grid, steps+1, checkedList)
    if [x+1,y] not in checkedList:
        right = findClosest(x+1, y, grid, steps+1, checkedList)
    if [x,y+1] not in checkedList:
        up = findClosest(x, y+1, grid, steps+1, checkedList)
    if [x,y-1] not in checkedList:
        down = findClosest(x, y-1, grid, steps+1, checkedList)

    answer = min(left,right,up,down)
    print(answer)


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
        grid[x][y] = str(i+1) + '' + str(i+1)

    print(grid)

    for x in range(largestX):
        for y in range(largestY):
            checkedList = []
            findClosest(x,y, grid, 0, checkedList)


