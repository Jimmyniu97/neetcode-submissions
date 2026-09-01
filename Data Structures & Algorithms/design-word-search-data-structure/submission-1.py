class TrieNode():
    def __init__(self):
        self.children = dict()
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            character = word[i]
            if character not in node.children:
                node.children[character] = TrieNode()
            node = node.children[character]
            
        node.end = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            for j in range(i, len(word)):
                character = word[j]
                if character == ".":
                    for child in node.children.values():
                        if dfs(j+1, child):
                            return True
                    return False
                else:
                    if character not in node.children:
                        return False
                    node = node.children[character]
            return node.end
        
        return dfs(0, self.root)
            