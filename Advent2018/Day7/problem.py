import os
import sys

os.chdir(sys.path[0])

class Node():
    def __init__(self, letter):
        self.letter = letter
        self.children = []
    def __str__(self):
        return self.letter

class problemTree():
    def __init__(self):
        self.root = None
        self.seen = set()
    def add(self, pair, root=None):
        if root is None:
            root = self.root
        if self.root == None:
            self.root = Node(pair[0])
            self.root.children.append(Node(pair[1]))
            self.seen.add(pair[0])
            self.seen.add(pair[1])
        else:
            if pair[0] in self.seen:
                if root.letter == pair[0]:
                    root.children.append(Node(pair[1]))
                    self.seen.add(pair[0])
                    self.seen.add(pair[1])
                    return
                else:
                    for child in root.children:
                        self.add(pair, child)
            else:
                newNode = Node(pair[0])
                if newNode.letter < root.letter:
                    temp = self.root
                    self.root = newNode
                    newNode.children.append(temp)
                    self.seen.add(pair[0])
                    self.seen.add(pair[1])
                else:
                    root.children.append(newNode)
                    self.seen.add(pair[0])
                    self.seen.add(pair[1])


def parseLine(line):
    first = line[line.index('p')+2]
    second = line[-12]
    return [first, second]

with open('input.txt') as input:
    lines = [x.rstrip('\n') for x in input.readlines()]
    lines = [parseLine(x) for x in lines]
    # print(lines)

    tree = problemTree()
    for line in lines:
        tree.add(line)

    print('hi')
