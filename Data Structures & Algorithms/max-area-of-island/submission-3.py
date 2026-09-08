from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(r, c):
            grid[r][c] = 0
            queue = deque([(r, c)])
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            area = 0

            while queue:
                row, col = queue.popleft()
                area += 1
                for dr, dc in directions:
                    i, j = row+dr, col+dc
                    if (0 <= i < ROWS and 0 <= j < COLS and grid[i][j] == 1):
                        grid[i][j] = 0
                        queue.append((i, j))
            
            return area
        
        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    ans = max(bfs(r, c), ans)
        
        return ans
