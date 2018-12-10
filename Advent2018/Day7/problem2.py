import os
import sys
from string import ascii_uppercase

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

    sorted(dependencyMap)

    while len(letterOrder) < 26:
        for key,value in dependencyMap.items():
            if set(value).issubset(set(letterOrder)):
                letterOrder.append(key)
                del dependencyMap[key]
                break

    print(letterOrder)
    print(''.join(x for x in letterOrder))