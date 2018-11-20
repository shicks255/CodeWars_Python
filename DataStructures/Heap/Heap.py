
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

    def getParent(self, index):
        if index == 0:
            return None
        if index % 2 == 0:
            answerIndex = int((index / 2) - 1)
        else:
            answerIndex = int((index-1) / 2)
        return [answerIndex, self.values[answerIndex]]

    def addValue(self, value):
        self.values.append(value)
        self.heapifyUp()

    def pop(self):
        item = self.values.pop(0)
        self.heapifyDown()
        return item

    def heapifyUp(self):
        index = len(self.values)-1
        while (index > 0):
            parentTup = self.getParent(index)
            if parentTup is not None:
                if parentTup[1] < self.values[index]:
                    temp = self.values[parentTup[0]]
                    self.values[parentTup[0]] = self.values[index]
                    self.values[index] = temp
            index -= 1


    def heapifyDown(self, index = None):
        if index is None:
            index = 0

        rightChild = self.getRightChild(index)
        leftChild = self.getLeftChild(index)

        if rightChild is not None or leftChild is not None:
            if leftChild[1] > self.values[index]:
                temp = self.values[leftChild[0]]
                self.values[leftChild[0]] = self.values[index]
                self.values[index] = temp
                self.heapifyDown(index)
            if rightChild[1] > self.values[index]:
                temp = self.values[rightChild[0]]
                self.values[rightChild[0]] = self.values[index]
                self.values[index] = temp
                self.heapifyDown(index)
            index += 1

