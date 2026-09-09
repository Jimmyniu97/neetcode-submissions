from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31-1
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque([])
        visited = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    queue.append((r, c))
        
        dist = 0
        while queue:
            qLen = len(queue)
            for _ in range(qLen):
                curr = queue.popleft()
                r, c = curr
                grid[r][c] = dist
                for dr, dc in directions:
                    i, j = r+dr, c+dc
                    if (0 <= i < ROWS and 0 <= j < COLS and (i,j) not in visited and grid[i][j] == INF):
                        visited.add((i,j))
                        queue.append((i,j))
                    

            dist += 1