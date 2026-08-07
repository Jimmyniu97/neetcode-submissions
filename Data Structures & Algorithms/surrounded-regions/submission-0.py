class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        def dfs(i,j):
            board[i][j] = "#"
            for x,y in directions:
                row = x+i
                col = y+j
                if 0 <= row < rows and 0 <= col < cols and board[row][col] == "O":
                    dfs(row, col)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i == 0 or i == rows-1 or j == 0 or j == cols-1):
                    dfs(i,j)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
