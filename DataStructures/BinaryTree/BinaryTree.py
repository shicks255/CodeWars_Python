
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

    def preOrder(self, function, root=None):
        if root is None:
            root = self.root

        function(root.value)

        if root.left is not None:
            self.preOrder(function, root=root.left)
        if root.right is not None:
            self.preOrder(function, root=root.right)

    def inOrder(self, function, root=None):
        if root is None:
            root = self.root

        if root.left is not None:
            self.inOrder(function, root=root.left)

        function(root.value)

        if root.right is not None:
            self.inOrder(function, root=root.right)

    def postOrder(self, function, root=None):
        if root is None:
            root = self.root

        if root.left is not None:
            self.postOrder(function, root=root.left)
        if root.right is not None:
            self.postOrder(function, root=root.right)

        function(root.value)

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

    def sumOfNodes(self):
        sum = 0
        queue = Queue()
        queue.enqueue(self.root)
        while queue.isEmpty() == False:
            node = queue.dequeue().value
            sum += node.value
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)

        return sum

    # sum of largest path
    def maxSumPath(self, root=None):
        if root is None:
            root = self.root

        if root is not None:
            if root.left is None and root.right is None:
                return root.value

            countLeft = root.value
            countRight = root.value

            if root.left is not None:
                countLeft += self.maxSumPath(root.left)
            if root.right is not None:
                countRight += self.maxSumPath(root.right)

            return max(countLeft, countRight)

        return 0
























