# !python 3

class node():

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return 'this node value is ' + str(self.value)


