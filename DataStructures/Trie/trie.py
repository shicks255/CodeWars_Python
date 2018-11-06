
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

    def doesWordExist(self, word):
        dic = self.root
        tempNode = None
        for let in word:
            if let in dic:
                tempNode = dic[let]
                dic = tempNode.letters
            else:
                return False

        if tempNode is not None and tempNode.leaf:
            return True

        return False

    def getCountOfPrefixes(self, word):
        if self.root is not None:
            prefixes = 0
            letters = self.root
            for i,x in enumerate(word):
                if x not in letters:
                    return 0
                if i != len(word)-1:
                    child = letters[x]
                    if child.leaf:
                       prefixes += 1
                    letters = child.letters

            return prefixes


