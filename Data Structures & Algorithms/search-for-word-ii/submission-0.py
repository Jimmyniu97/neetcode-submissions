class TrieNode:
    def __init__(self):
        self.children = dict()
        self.index = -1

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, index):
        node = self.root
        for character in word:
            if character not in node.children:
                node.children[character] = TrieNode()
            node = node.children[character]
        node.index = index

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(r, c, node):
            character = board[r][c]
            node = node.children[character]
            if node.index != -1:
                result.append(words[node.index])
                node.index = -1
            temp = board[r][c]
            board[r][c] = '#'

            for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                row = r + x
                col = c + y
                if (0 <= row < len(board) and 0 <= col < len(board[0])) and board[row][col] in node.children:
                    dfs(row, col, node)
            
            board[r][c] = temp


        result = []
        T = Trie()
        for index, word in enumerate(words):
            T.insert(word, index)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in T.root.children:
                    dfs(i, j, T.root)
        
        return result
           