
import os
import sys
import re
from collections import deque

os.chdir(sys.path[0])

def parseInput(line):
    regex = re.compile(r'(\d+)')
    mo = regex.findall(line)
    if mo:
        return [int(mo[0]), int(mo[1])]
with open("input.txt") as input:
    line = input.readlines()[0]
    list = deque()
    playersAndMarbles = parseInput(line)

    print(playersAndMarbles)


