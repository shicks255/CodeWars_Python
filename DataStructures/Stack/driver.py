# !python3
# import DataStructures.Stack.Stack as Stack
from DataStructures.Stack.Stack import Stack


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.prettyPrint()
stack.pop()
stack.pop()
stack.prettyPrint()