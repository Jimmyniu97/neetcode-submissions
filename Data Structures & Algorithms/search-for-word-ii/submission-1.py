class TrieNode():
    def __init__(self):
        self.children = dict()
        self.end = False
        self.index = -1
    
    def add(self, word):
        node = self
        for character in word:
            if character not in node.children:
                node.children[character] = TrieNode()
            node = node.children[character]
        node.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.add(word)
        
        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(i, j, node, word):
            if (i < 0 or i >= ROWS or j < 0 or
             j >= COLS or (i, j) in visited or
              board[i][j] not in node.children):
              return
            
            visited.add((i, j))
            node = node.children[board[i][j]]
            word += board[i][j]
            if node.end:
                res.add(word)
            
            dfs(i + 1, j, node, word)
            dfs(i - 1, j, node, word)
            dfs(i, j + 1, node, word)
            dfs(i, j - 1, node, word)
            visited.remove((i, j))
        

        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, root, "")
        
        return list(res)



