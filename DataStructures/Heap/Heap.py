
class Heap():

    def __init__(self, initialValue):
        self.values = []
        self.values.append(initialValue)

    def getLeftChild(self, index):
        answerIndex = (index * 2) + 1
        if len(self.values) > answerIndex:
            return [answerIndex, self.values[answerIndex]]
        else:
            return None
    def getRightChild(self, index):
        answerIndex = (index * 2) + 2
        if len(self.values) > answerIndex:
            return [answerIndex, self.values[answerIndex]]
        else:
            return None

    def addValue(self, value):
        self.values.append(value)
        # need heapify up function

    def pop(self):
        return self.values.pop()
        # need heapify down
