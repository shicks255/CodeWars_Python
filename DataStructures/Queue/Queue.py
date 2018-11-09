# !python3

from DataStructures.Queue.Node import Node

class Queue():

    def __init__(self):
        self.head = None

    def enqueue(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            tempHead = self.head
            while tempHead.next is not None:
                tempHead = tempHead.next
            tempHead.next = Node(value)

    def dequeue(self):
        tempHead = self.head
        if tempHead is not None:
            if tempHead.next is None:
                self.head = None
            if tempHead.next is not None:
                self.head = tempHead.next
        return tempHead

    def prettyPrint(self):
        tempHead = self.head
        coursor = 1
        while tempHead is not None:
            print('position ' + str(coursor) + ' is ' + str(tempHead.value))
            coursor += 1
            tempHead = tempHead.next

    def isEmpty(self):
        return self.head is None
