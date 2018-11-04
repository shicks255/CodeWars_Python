
from DataStructures.Trie.Node import Node

class Trie():

    def __init__(self):
        self.root = {}

    def addString(self, string):
        dic = self.root
        for i,let in enumerate(string, 1):
            if let not in dic:
                dic[let] = Node(let)
            if i == len(string):
                dic[let].leaf = True
            dic = dic[let].letters


