
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
            answerIndex = int((index-2 / 2))
        return [answerIndex, self.values[answerIndex]]

    def addValue(self, value):
        self.values.append(value)
        self.heapifyUp()

    def pop(self):
        return self.values.pop()
        # need heapify down


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


    # def heapifyDown(self):
    #     df