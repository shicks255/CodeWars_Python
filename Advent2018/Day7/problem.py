import os
import sys

os.chdir(sys.path[0])

class Node():
    def __init__(self, letter):
        self.letter = letter
        self.children = []

class problemTree():
    def __init__(self):
        self.root = None
    def add(self, pair, root=None):
        if root is None:
            root = self.root
        if self.root == None:
            self.root = Node(pair[0])
            self.root.children.append(Node(pair[1]))
        else:
            if root.letter == pair[0]:
                root.children.append(Node(pair[1]))
                return
            else:
                for child in root.children:
                    self.add(pair, child)
#             this will hit if we didnt find a match
            newNode = Node(pair[0])
            if newNode.letter < root.letter:
                temp = self.root
                self.root = newNode
                newNode.children.append(temp)
            else:
                root.children.append(newNode)



def parseLine(line):
    first = line[line.index('p')+2]
    second = line[-12]
    return [first, second]

with open('input.txt') as input:
    lines = [x.rstrip('\n') for x in input.readlines()]
    lines = [parseLine(x) for x in lines]
    print(lines)

    tree = problemTree()
    for line in lines:
        tree.add(line)

    print('hi')
