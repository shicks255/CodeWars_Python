# !python3

from DataStructures.LinkedList.linkedList import linkedList

list = linkedList()

list.add(1)
list.add(2)
list.add(3)
list.add(4)
list.add(5)

list.prettyPrint()

node = list.find(4)
print(node)

node2 = list.find(2)
print(node2)

list.remove(1)
list.remove(5)
list.remove(5)
list.prettyPrint()