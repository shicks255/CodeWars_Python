
import os
import sys
import re

os.chdir(sys.path[0])

class LinkedList():
    def __init__(self):
        self.root = None
        self.current = None


class Node():
    def __init__(self):
        self.next = None
        self.previous = None
        self.data = None

def parseInput(line):
    regex = re.compile(r'(\d+)')
    mo = regex.findall(line)
    if mo:
        return [int(mo[0]), int(mo[1])]
with open("input.txt") as input:
    line = input.readlines()[0]
    playersAndMarbles = parseInput(line)

    print(playersAndMarbles)
    playerScores = {}
    for x in range(playersAndMarbles[0]):
        playerScores[x+1] = 0

    list = LinkedList()

    playerCounter = 1
    for x in range((playersAndMarbles[1]*100)+1):
        if x % 23 == 0 and x != 0:
            toAdd = x
            node1 = list.current
            for _ in range(7):
                node1 = node1.previous
            toAdd += node1.data
            playerScores[playerCounter] += toAdd
            nodeRight = node1.next
            nodeLeft = node1.previous
            nodeRight.previous = nodeLeft
            nodeLeft.next = nodeRight
            list.current = nodeRight
        elif list.root is not None:
            node1 = list.current.next
            node2 = node1.next
            node = Node()

            node.data = x
            node1.next = node

            node.previous = node1
            node.next = node2
            node2.previous = node
            list.current = node
        elif list.root is None:
            node = Node()
            node.data = x
            node.next = node
            node.previous = node
            list.root = node
            list.current = node
            playerCounter -= 1

        playerCounter += 1
        if playerCounter > playersAndMarbles[0]:
            playerCounter = 1

        print(list.current.data)

    print(list)
    winner = max(playerScores.values())
    print(winner)


