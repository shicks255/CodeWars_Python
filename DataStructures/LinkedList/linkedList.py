# !python 3

from DataStructures.LinkedList.node import node

class linkedList():

    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = node(value)
        else:
            tempNode = self.root
            while tempNode.next is not None:
                tempNode = tempNode.next

            tempNode.next = node(value)

    def find(self, value):
        tempNode = self.root
        while tempNode is not None:
            if tempNode.value == value:
                return tempNode
            tempNode = tempNode.next

    # def remove(self, value):


    def prettyPrint(self):
        theNode = self.root
        cursor = 1
        while theNode is not None:
            print(str(theNode.value) + ' ' + str(cursor))
            cursor += 1
            theNode = theNode.next