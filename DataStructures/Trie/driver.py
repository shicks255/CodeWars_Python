from DataStructures.Trie.Trie import Trie

trie = Trie()

trie.addString('pen')
trie.addString('pot')
trie.addString('penis')
trie.addString('pencil')

print(trie.doesWordExist('pen'))
print(trie.doesWordExist('peo'))
print(trie.doesWordExist('pencils'))
print(trie.doesWordExist('pencil'))
