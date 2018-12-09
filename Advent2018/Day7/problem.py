import os
import sys

os.chdir(sys.path[0])

class Node():
    def __init__(self, letter):
        self.letter = letter
        self.children - []

class problemTree():
    def __init__(self, letter):
        self.root = Node(letter)

def parseLine(line):
    first = line[line.index('p')+2]
    second = line[-12]
    return [first, second]


with open('input.txt') as input:
    lines = [x.rstrip('\n') for x in input.readlines()]
    lines = [parseLine(x) for x in lines]
    print(lines)



