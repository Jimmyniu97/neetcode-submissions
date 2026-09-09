from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        
        level = 0
        while queue and fresh > 0:
            qLen = len(queue)
            for _ in range(qLen):
                r, c = queue.popleft()
                for dr, dc in directions:
                    i, j = r+dr, c+dc
                    if (0 <= i < ROWS and 0 <= j < COLS and grid[i][j] == 1):
                        grid[i][j] = 2
                        queue.append((i, j))
                        fresh -= 1
            level += 1
        
        return level if fresh == 0 else -1
