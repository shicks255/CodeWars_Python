
from DataStructures.BinaryTree.Node import Node
from DataStructures.Queue.Queue import Queue


class BinaryTree():

    def __init__(self, value):
        self.root = Node(value)
        self.root.leaf = False

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

    # this probably needs pre order traversal
    def height(self, root=None):
        if root is None:
            root = self.root
        leftValue = None
        rightValue = None
        if root.left is None:
            leftValue = 0
        else:
            leftValue = self.height(root.left)

        if root.right is None:
            rightValue = 0
        else:
            rightValue = self.height(root.right)

        if leftValue > rightValue:
            return leftValue + 1
        else:
            return rightValue + 1

    def preOrder(self, root=None):
        if root is None:
            root = self.root

        print(root.value)

        if root.left is not None:
            self.preOrder(root.left)
        if root.right is not None:
            self.preOrder(root.right)

    def inOrder(self, root=None):
        if root is None:
            root = self.root

        if root.left is not None:
            self.inOrder(root.left)

        print(root.value)

        if root.right is not None:
            self.inOrder(root.right)

    def postOrder(self, root=None):
        if root is None:
            root = self.root

        if root.left is not None:
            self.postOrder(root.left)
        if root.right is not None:
            self.postOrder(root.right)

        print(root.value)

    def nodeCount(self):
        queue = Queue()
        queue.enqueue(self.root)
        count = 0
        while queue.isEmpty() == False:
            node = queue.dequeue().value
            if node is not None:
                count +=1
                queue.enqueue(node.left)
                queue.enqueue(node.right)
        return count


    def leafCount(self):
        queue = Queue()
        if self.root is not None:
            queue.enqueue(self.root)
            count = 0
            while queue.isEmpty() == False:
                node = queue.dequeue().value
                if node is not None:
                    if node.left is None and node.right is None:
                        count += 1
                    else:
                        queue.enqueue(node.left)
                        queue.enqueue(node.right)
            return count

    def levelCount(self, level):
        if self.root is not None:
            count = 1

    # assuming 0 is root
    def getNodeCountAtLevel(self, level, root=None):
        if level == 0:
            return 1

        if root is None:
            root = self.root

        count = 0

        if root.left is not None:
            count += self.getNodeCountAtLevel(level-1, root.left)
        if root.right is not None:
            count += self.getNodeCountAtLevel(level-1, root.right)

        return count






