import os
import sys
import collections

os.chdir(sys.path[0])
file = open("ids.txt")
ids = file.readlines()
ids = [x.rstrip('\n') for x in ids]

# part 1
twos = 0
threes = 0
for id in ids:
    lookingForTwo = True
    lookingForThree = True
    counter = collections.Counter(id)
    for key in counter.keys():
        if counter[key] == 2 and lookingForTwo:
            twos += 1
            lookingForTwo = False
        if counter[key] == 3 and lookingForThree:
            threes += 1
            lookingForThree = False

print(twos)
print(threes)
print(twos * threes)

# part 2 --have an n2 solution but it works.
for id in ids:
    for id2 in ids:
        if id == ids:
            continue
        countOfDifferences = 0
        letterCount = len(id)
        for x, val in enumerate(id):
            if val != id2[x]:
                countOfDifferences += 1
        if countOfDifferences == 1:
            answer = ''
            for x, val in enumerate(id):
                if val == id2[x]:
                    answer += val
            print(answer)