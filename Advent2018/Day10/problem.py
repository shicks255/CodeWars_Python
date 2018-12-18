
import sys

import os

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

with open('testInput.txt') as input:
    coords = parseInput(input.readlines())

    helpInfo = findHomePoint(coords)
    homePoint = helpInfo['home']
    homePoint[0] = abs(homePoint[0])
    homePoint[1] = abs(homePoint[1])
    print(helpInfo)

    totalx = abs(helpInfo['bx']) + abs(helpInfo['sx']) + 1
    totaly = abs(helpInfo['by']) + abs(helpInfo['sy']) + 1

    grid = [['.' for x in range(totalx)] for y  in range(totaly)]

    while True:
        for coord in coords:
            x = coord[0] + homePoint[0]
            y = coord[1] + homePoint[1]
            grid[y][x] = '#'

        print('\n'.join([' '.join([cell for cell in row]) for row in grid]))
        grid = [['.' for x in range(totalx)] for y  in range(totaly)]
        changeCoords(coords)


