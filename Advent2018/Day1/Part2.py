import os
import sys

os.chdir(sys.path[0])
file = open("frequencies.txt")
frequencies = file.readlines()
frequencies = [int(x.rstrip('\n')) for x in frequencies]

answer = None
adder = 0
theSet = set()
while answer is None:
    for x in frequencies:
        adder = adder + x;
        if adder in theSet:
            answer = adder
            break;
        if adder not in theSet:
            theSet.add(adder)

print(answer)