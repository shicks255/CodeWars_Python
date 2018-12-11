import os
import sys
from string import ascii_uppercase
from queue import Queue

os.chdir(sys.path[0])

def parseLine(line):
    first = line[line.index('p')+2]
    second = line[-12]
    return [first, second]

with open('input.txt') as input:
    lines = [x.rstrip('\n') for x in input.readlines()]
    lines = [parseLine (x) for x in lines]
    # print(lines)

    dependencyMap = {}
    for x in ascii_uppercase:
        dependencyMap[x] = []

    for line in lines:
        if line[1] not in dependencyMap.keys():
            dependencyMap[line[1]] = []
        dependencyMap[line[1]].append(line[0])

    letterOrder = []

    alphaNumbers = {'A':61,'B':62,'C':63,'D':64,'E':65,'F':66,'G':67,'H':68,'I':69,'J':70,'K':71,'L':72,'M':73,'N':74,'O':75,'P':76,'Q':77,'R':78,'S':79,'T':80,'U':81,'V':82,'W':83,'X':84,'Y':85,'Z':86}

    sorted(dependencyMap)
    dependencyMapCopy = dict(dependencyMap)

    while len(letterOrder) < 26:
        for key,value in dependencyMap.items():
            if set(value).issubset(set(letterOrder)):
                letterOrder.append(key)
                del dependencyMap[key]
                break

    print(letterOrder)
    print(''.join(x for x in letterOrder))

    # part 2
    totalTime = -1
    queue = Queue()
    lettersUsed = []
    keepGoing = True
    workers = [[0,0],[0,0],[0,0],[0,0],[0,0]]
    lettersToBeWorked = None
    lettersBeingWorked = []
    while keepGoing:
        lettersToBeWorked = [x for x in dependencyMapCopy.keys() if set(dependencyMapCopy[x]).issubset(set(lettersUsed)) and x not in lettersBeingWorked and x not in lettersUsed]

        for x,worker in enumerate(workers):
            # empty, so put a letter in
            if worker[0] == 0 and worker[1] == 0:
                if len(lettersToBeWorked) > 0:
                    let = lettersToBeWorked.pop(0)
                    if let not in lettersBeingWorked:
                        worker[0] = let
                        worker[1] = alphaNumbers[let]
                        lettersBeingWorked.append(let)
            else:
                worker[1] -= 1
                if worker[1] <= 0:
                    let = worker[0]
                    lettersUsed.append(let)
                    lettersBeingWorked.remove(let)
                    worker[0] = 0
                    worker[1] = 0
                    lettersToBeWorked = [x for x in dependencyMapCopy.keys() if set(dependencyMapCopy[x]).issubset(set(lettersUsed)) and x not in lettersBeingWorked and x not in lettersUsed]
                    if len(lettersToBeWorked) > 0:
                        let = lettersToBeWorked.pop(0)
                        if let not in lettersBeingWorked:
                            worker[0] = let
                            worker[1] = alphaNumbers[let]
                            lettersBeingWorked.append(let)

        if len(lettersUsed) == 26:
            keepGoing = False
            break
        totalTime += 1

    print(totalTime)
