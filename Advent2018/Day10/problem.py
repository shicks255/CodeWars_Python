
import sys
import os
import time

os.chdir(sys.path[0])

def parseInput(input):
    input = [x.rstrip('\n') for x in input]
    coords = []
    for x in input:
        firstBracket = x.index('<')+1
        secondBracket = x.index('>')
        stuff = x[firstBracket:secondBracket]
        s = stuff.split(',')
        px = int(s[0])
        py = int(s[1])

        thirdBracket = x.index('<', secondBracket) +1
        fourthBracket = x.index('>', thirdBracket)
        stuff2 = x[thirdBracket : fourthBracket]
        s2 = stuff2.split(',')
        vx = int(s2[0])
        vy = int(s2[1])

        coords.append([px,py,vx,vy])
    return coords

def findHomePoint(coords):
    biggestX = 0
    smallestX = 0
    biggestY = 0
    smallestY = 0

    for coord in coords:
        if coord[0] > biggestX: biggestX = coord[0]
        if coord[0] < smallestX: smallestX = coord[0]
        if coord[1] > biggestY: biggestY = coord[1]
        if coord[1] < smallestY: smallestY = coord[1]

    homePoint = [smallestX, smallestY]

    helpInfo = {'bx': biggestX, 'sx': smallestX, 'by': biggestY, 'sy': smallestY, 'home': homePoint}
    return helpInfo

def changeCoords(coords):
    for coord in coords:
        coord[0] = coord[0] + coord[2]
        coord[1] = coord[1] + coord[3]

with open('input.txt') as input:
    coords = parseInput(input.readlines())

    helpInfo = findHomePoint(coords)
    homePoint = helpInfo['home']
    homePoint[0] = abs(homePoint[0])
    homePoint[1] = abs(homePoint[1])
    print(helpInfo)

    seconds = 0;

    file = open('answer.txt', 'a+')
    keepGoing = True
    while keepGoing:
        helpInfo2 = findHomePoint(coords)
        home = helpInfo2['home']
        if abs(home[0]) < 100 and abs(home[1]) < 100:
            totalx = abs(helpInfo2['bx']) + abs(helpInfo2['sx']) + 1
            totaly = abs(helpInfo2['by']) + abs(helpInfo2['sy']) + 1
            grid = [['.' for x in range(totalx)] for y  in range(totaly)]
            for coord in coords:
                x = coord[0] + home[0]
                y = coord[1] + home[1]
                grid[y][x] = '#'

            print('\n'.join([' '.join([cell for cell in row]) for row in grid]))
            print('\n\n')
            file.write('\n'.join([''.join([cell for cell in row]) for row in grid]))
            file.write('\n' + str(seconds) + ' seconds')
            file.write('\n\n')
            time.sleep(2)
            grid = [['.' for x in range(totalx)] for y  in range(totaly)]
        seconds += 1
        changeCoords(coords)

    file.close()
