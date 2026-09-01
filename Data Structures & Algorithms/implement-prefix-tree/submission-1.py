class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            character = word[i]
            if character in node.children:
                node = node.children[character]
            else:
                node.children[character] = TrieNode()
                node = node.children[character]
            
            if i == len(word)-1:
                node.end = True

    def search(self, word: str) -> bool:
        i = 0
        node = self.root
        while i < len(word):
            character = word[i]
            if character not in node.children:
                return False
            else:
                node = node.children[character]
            i += 1
        
        return node.end

    def startsWith(self, prefix: str) -> bool:
        i = 0 
        node = self.root
        while i < len(prefix):
            character = prefix[i]
            if character not in node.children:
                return False
            else:
                node = node.children[character]
            i += 1
        
        return True
        