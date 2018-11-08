
from DataStructures.BinaryTree.Node import Node

class BinaryTree():

    def __init__(self, value):
        self.root = Node(value)
        self.root.leaf = False

    # def addNode(self, value):
    #     self.addNode(self, self.root, value)

    def addNode(self, value, root=None):
        if root is None:
            root = self.root
        if value < root.value:
            if root.left is None:
                root.left = Node(value)
            else:
                self.addNode(value, root=root.left)

        if value >= root.value:
            if root.right is None:
                root.right = Node(value)
            else:
                self.addNode(value, root=root.right)

    def isEmpty(self):
        return self.root is None

    def height(self):
        height = 0


    # def nodeCount(self):
    #
    # def leafCount(self):
    #
    # def levelCount(self, level):
