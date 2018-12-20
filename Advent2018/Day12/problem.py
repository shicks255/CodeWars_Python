
import os
import sys

os.chdir(sys.path[0])

def generation():
    newState = ''
    for i,x in enumerate(initialState):
        if i < 2 or i > len(initialState)-2:
            newState += '.'
            continue
        if initialState[i-2:i+3] in notesMap.keys():
            v = notesMap[initialState[i-2:i+3]]
            if v == '#':
                newState += '#'
            if v != '#':
               newState += '.'
        else:
            newState += '.'
    return newState



with open('testInput.txt') as input:
    lines = input.readlines()
    initialState = '..........' + lines[0][lines[0].index('#'):-1] + '...........'
    initialState.replace('\n', '')
    notes = [x.rstrip('\n') for x in lines[2:]]
    notesMap = {x.split('=>')[0].strip(): x.split('=>')[1].strip() for x in notes}

    totalPlants = 0

    for x in range(21):
        print(x)
        for xx,yy, in enumerate(initialState):
            if yy == '#':
                totalPlants += (xx-10)
        # totalPlants += len([i for i in initialState if i == '#'])
        print(totalPlants)
        print(initialState)

        initialState = generation()

    print(totalPlants)
