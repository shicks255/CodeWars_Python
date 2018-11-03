# !python3

from DataStructures.Queue.Queue import Queue

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.prettyPrint()

queue.dequeue()
queue.dequeue()
queue.prettyPrint()