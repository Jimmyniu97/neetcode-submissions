class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        
        def bfs(r, c):
            queue = collections.deque([(r,c)])
            visited = {(r,c)}
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            edge = False if (r > 0 and r < ROWS-1 and c > 0 and c < COLS-1) else True
            while queue and not edge:
                row, col = queue.popleft()
                for dr, dc in directions:
                    i, j = row+dr, col+dc
                    if (0 <= i < ROWS and 0 <= j < COLS and (i,j) not in visited and board[i][j] == "O"):
                        if (i == 0 or i == ROWS-1 or j == 0 or j == COLS-1):
                            edge = True
                            break
                        visited.add((i,j))
                        queue.append((i,j))
            
            if not edge:
                for r, c in visited:
                    board[r][c] = "X"
        

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    bfs(r, c)
