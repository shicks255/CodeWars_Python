
class Node():

    def __init__(self,value):
        self.value = value
        self.leaf = True
        self.left = None
        self.right = None

    def __str__(self):
        return 'node value of ' + str(self.value)