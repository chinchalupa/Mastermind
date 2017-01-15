import settings

class Trie:
    def __init__(self, keyList, depth):
        self.keyList = keyList
        self.depth = depth
        self.root = TrieNode(keyList, depth)

    def getDepth(self, depth):
        if depth == 0:
            return ''
        array = []
        for key in self.root.getChildren().keys():
            array += self.root.getChildren()[key].getNodesAtDepth(depth - 1, key)
        return array

class TrieNode:
    def __init__(self, keyList, depth):
        self.map = {}
        self.generate(keyList, depth)

    def generate(self, keyList, depth):
        if depth == 0:
            return
        for key in keyList:
            self.map[key] = TrieNode(keyList, depth - 1)

    def getChildren(self):
        return self.map

    def getNodesAtDepth(self, depth, code):
        if depth == 0:
            return [code]
        array = []
        for key in self.map.keys():
            array += self.map[key].getNodesAtDepth(depth - 1, code + key)
        return array




trie = Trie(settings.COLORS, len(settings.COLORS))
print trie.root.getChildren()['B'].getChildren()['B']
print str(trie.getDepth(4))

