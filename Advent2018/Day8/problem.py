
import os
import sys

os.chdir(sys.path[0])

class Node():
    def __init__(self):
        self.childNodes = []
        self.metaData = []

rootNode = None
def makeNode(startIndex):
    numberOfChildren = license[startIndex]
    startIndex += 1
    numberOfMeta = license[startIndex]
    startIndex += 1

    node = Node()
    for x in range(numberOfChildren):
        returnValue = makeNode(startIndex)
        node.childNodes.append(returnValue[0])
        startIndex = returnValue[1]

    meta = license[startIndex:startIndex+numberOfMeta]
    startIndex += len(meta)
    node.metaData = meta
    global rootNode
    if rootNode is None:
        rootNode = node

    return [node, startIndex]

def getPart2(node):
    if len(node.childNodes) == 0:
        return sum(node.metaData)
    else:
        sum2 = 0
        meta = node.metaData
        for x in meta:
            if len(node.childNodes) > x-1:
                child = node.childNodes[x-1]
                sum2 += getPart2(child)
        return sum2

with open("input.txt") as input:
    line = input.readlines()
    license = [int(x) for x in str.split(line[0], ' ')]
    rootTuple = makeNode(0)

    print(rootTuple)

    sumOfMeta = 0
    nodes = []
    nodes.append(rootTuple[0])
    while len(nodes) > 0:
        node = nodes.pop(0)
        nodes += node.childNodes
        sumOfMeta += sum(node.metaData)

    print(sumOfMeta)

    sum2 = getPart2(rootTuple[0])
    print(sum2)







