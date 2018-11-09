
from DataStructures.BinaryTree.Node import Node
from DataStructures.Queue.Queue import Queue
from DataStructures.Queue.Node import Node as QueueNode

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
    def height(self):
        height = 0

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

    # def levelCount(self, level):
