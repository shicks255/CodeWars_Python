
from DataStructures.BinaryTree.BinaryTree import BinaryTree as Tree


tree = Tree(15)

tree.addNode(12)
tree.addNode(4)
tree.addNode(1)
tree.addNode(16)
tree.addNode(18)
tree.addNode(17)
tree.addNode(19)
tree.addNode(20)

# tree.preOrder(lambda x: print(x))

print(tree.sumOfNodes())



# tree.addNode(3)
# tree.addNode(4)
# tree.addNode(1)
# tree.addNode(24)

# print(tree.getNodeCountAtLevel(3))
#
# print('hi')

# print(tree.nodeCount())
# print(tree.leafCount())
# print(tree.height())

# tree.postOrder()