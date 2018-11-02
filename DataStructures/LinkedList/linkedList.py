# !python 3

import DataStructures.LinkedList.node as node

class linkedList():

    def add(self, value):
        if self.root is None:
            self.root = node(value)
        else:
            tempRoot = self.root
            while tempRoot.next is not None:
                tempRoot = tempRoot.next

            tempRoot.next = node(value)

