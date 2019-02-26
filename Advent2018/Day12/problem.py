
import os
import sys

os.chdir(sys.path[0])

startingIndex = 0

def generation(initialState):
    state = list(initialState)

    addToBeginning = False
    addToEnd = False

    leftTest = '...'
    for x in state[0:2]:
        leftTest += str(x)
    if leftTest in notesMap.keys():
        if notesMap[leftTest] == '#':
            addToBeginning = True
            global startingIndex
            startingIndex += 1

    rightTest = ''
    for x in state[len(state)-2:]:
        rightTest += str(x)
    rightTest += '...'
    if rightTest in notesMap.keys():
        if notesMap[rightTest] == '#':
            addToEnd = True

    for i,x in enumerate(initialState):
        goLeft = i-2
        goRight = i+3
        lookingFor = initialState[goLeft:goRight]
        if i == 0:
            goLeft = i
            lookingFor = '..' + initialState[goLeft:goRight]
        if i == 1:
            goLeft = i-1
            lookingFor = '.' + initialState[goLeft:goRight]
        if i == len(initialState):
            goRight = i
            lookingFor = initialState[goLeft:goRight] + '...'
        if i == len(initialState)-1:
            goRight = i+1
            lookingFor = initialState[goLeft:goRight] + '..'

        if lookingFor in notesMap.keys():
            state[i] = '#'
            v = notesMap[lookingFor]
            if v == '#':
                state[i] = '#'
            if v != '#':
                state[i] = '.'
        else:
            state[i] = '.'

    if addToBeginning:
        state.insert(0, '#')
    if addToEnd:
        state.append('#')

    return ''.join(state)

with open('input.txt') as input:
    lines = input.readlines()
    initialState = lines[0][lines[0].index('#'):-1]
    initialState.replace('\n', '')
    notes = [x.rstrip('\n') for x in lines[2:]]
    notesMap = {x.split('=>')[0].strip(): x.split('=>')[1].strip() for x in notes}

    totalPlants = 0

    for x in range(20):
        print(str(x) + ' ' +  initialState)
        # print(initialState)
        initialState = generation(initialState)

    print('20 ' + initialState)
    for xx,yy, in enumerate(initialState):
        if yy == '#':
            totalPlants += (xx - startingIndex)


    print(totalPlants)
