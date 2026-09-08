from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        def bfs(r, c):
            grid[r][c] = '0'
            queue = deque([(r, c)])
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while queue:
                row, col = queue.popleft()
                for a, b in directions:
                    i, j = row + a, col + b
                    if (0 <= i < ROWS and 0 <= j < COLS and grid[i][j] == '1'):
                        grid[i][j] = '0'
                        queue.append((i, j))
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    bfs(r, c)
                    res += 1
        
        return res