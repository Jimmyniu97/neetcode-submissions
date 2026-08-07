class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."]*n for _ in range(n)]

        def valid(i, j):
            directions = [[0,-1],[-1,-1],[1,-1]]
            for x,y in directions:
                row = i+x
                col = j+y
                while 0 <= row < n and 0 <= col < n:
                    if board[row][col] == "Q":
                        return False
                    row += x
                    col += y
            return True
            
        
        def dfs(c):
            if c == n:
                res.append(["".join(i) for i in board.copy()])
                return
            
            for r in range(n):
                if valid(r, c):
                    board[r][c] = "Q"
                    dfs(c+1)
                    board[r][c] = "."
        
        dfs(0)
        return res
