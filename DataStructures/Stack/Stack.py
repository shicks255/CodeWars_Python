from DataStructures.Stack.Node import Node

class Stack():

    def __init__(self):
        self.top = None

    def push(self, value):
        if self.top is None:
            self.top = Node(value)
        else:
            tempNode = self.top
            self.top = Node(value)
            self.top.next = tempNode

    def pop(self):
        if self.top is not None:
            if self.top.next is not None:
                temp = self.top
                self.top = temp.next
                return temp
            else:
                temp = self.top
                self.top = None
                return temp

    def prettyPrint(self):
        if self.top is not None:
            temp = self.top
            coursor = 1
            while temp is not None:
                print('position ' + str(coursor) + ' contains value ' + str(temp.value))
                temp = temp.next
                coursor += 1