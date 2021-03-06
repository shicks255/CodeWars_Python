import os
import sys

os.chdir(sys.path[0])

def getSize(x, y):
    total = 0
    total += grid[y][x]
    total += grid[y][x+1]
    total += grid[y][x+2]
    total += grid[y+1][x]
    total += grid[y+1][x+1]
    total += grid[y+1][x+2]
    total += grid[y+2][x]
    total += grid[y+2][x+1]
    total += grid[y+2][x+2]
    return total

def getSizePart2(x, y, squareSize):
    total = 0

    for i in range(squareSize):
        for ii in range(squareSize):
            total += grid[y+i][x+ii]
    return total


with open("input.txt") as input:
    inputMulty = int(input.read())

    grid = [['0' for _ in range(300)] for _ in range(300)]
    # print('\n'.join([' '.join([cell for cell in row]) for row in grid]))

    for i,y in enumerate(grid):
        for ii,x in enumerate(y):
            rackId = ii+1 + 10
            powerLevel = rackId * (i+1)
            powerLevel += inputMulty
            powerLevel *= rackId
            if powerLevel > 100:
                powerLevel = int(str(powerLevel)[:-2][-1])
            else:
                powerLevel = 0
            powerLevel -= 5

            grid[i][ii] = powerLevel

    print('\n'.join([','.join([str(cell) for cell in row]) for row in grid]))

    # part 1 stuff
    # currentBiggest = [0, 0, 0]
    # for i,y in enumerate(grid):
    #     for ii,x in enumerate(y):
    #         if i > 297 or ii > 297:
    #             continue
    #         threeByThreeSize = getSize(ii, i)
    #         if threeByThreeSize > currentBiggest[0]:
    #             currentBiggest[0] = threeByThreeSize
    #             currentBiggest[1] = ii
    #             currentBiggest[2] = i

    # part 2 stuff
    currentBiggest = [0,0,0,0]
    for sq in range(1, 300):
        for i,y in enumerate(grid):
            for ii,x in enumerate(y):
                if i >(300 - sq) or ii > (300 - sq):
                    continue
                size = getSizePart2(ii, i, sq)
                if size > currentBiggest[0]:
                    currentBiggest[0] = size
                    currentBiggest[1] = ii
                    currentBiggest[2] = i
                    currentBiggest[3] = sq
        print(currentBiggest)

    print(currentBiggest)




