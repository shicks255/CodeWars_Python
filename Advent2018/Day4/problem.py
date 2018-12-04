import sys
import os

os.chdir(sys.path[0])

def parseRecord(record):
    record = str(record)
    timeIndex = record.index(']')
    time = record[timeIndex-5:timeIndex]
    date = record[1:11]
    action = record[timeIndex+2:]
    return [date, time, action]

def doSomething(map, currentGaurd, startingBatch, x, lines):
    startingBatch += 1
    x -= 1

    if currentGuard not in map:
        map[currentGuard] = [0 for x in range(60)]

    sleepMinutes = map[currentGuard]

    for i in range(x):
        line = lines[startingBatch+i]
        line = parseRecord(line)
        # even, or falling asleep
        if i % 2 == 0:
            asleepStart = line[1]
            if int(asleepStart[0:2]) != 0:
                asleepStart = '00:00'
        # odd, or waking up
        if i % 2 != 0:
            if asleepStart is not None:
                wakeUp = line[1]
                if int(wakeUp[0:2]) != 0:
                    wakeUp = '00:00'
                start = int(asleepStart[3:])
                end = int(wakeUp[3:])
                while start != end:
                    sleepMinutes[start] += 1
                    start += 1


with open("input.txt") as input:
    lines = [x.rstrip('\n') for x in input.readlines()]
    lines.sort()
    map = {}
    currentGuard = None
    startingBatch = 0
    for x,line in enumerate(lines):
        record = parseRecord(line)
        if '#' in record[2]:
            pieces = record[2].split(' ')
            if currentGuard is not None:
                doSomething(map, currentGuard, startingBatch, x-startingBatch, lines)
            currentGuard = int(pieces[1].replace('#',''))
            startingBatch = x

    mostGuardAndTotal = [0, 0]
    for x in map.keys():
        line = map[x]
        total = sum(line)
        if total > mostGuardAndTotal[1]:
            mostGuardAndTotal[0] = x
            mostGuardAndTotal[1] = total

    mostSleepyMinuteList = map[mostGuardAndTotal[0]]
    sleepiestMinute = max(mostSleepyMinuteList)
    for x,minute in enumerate(mostSleepyMinuteList):
        if minute == sleepiestMinute:
            print(x * mostGuardAndTotal[0])
            break

    part2GuardAndMinuteAndAmount = [0,0,0]
    for x in map.keys():
        line = map[x]
        maxDaysSleeping = max(line)
        if maxDaysSleeping > part2GuardAndMinuteAndAmount[2]:
            part2GuardAndMinuteAndAmount[0] = x
            part2GuardAndMinuteAndAmount[2] = maxDaysSleeping
            for x,minute in enumerate(line):
                if minute == maxDaysSleeping:
                    part2GuardAndMinuteAndAmount[1] = x
                    break

    print(part2GuardAndMinuteAndAmount)






