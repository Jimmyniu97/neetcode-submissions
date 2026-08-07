from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        rows, cols = len(grid), len(grid[0])
        ans = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
        
        while queue:
            i, j, dist = queue.popleft()
            ans = max(ans, dist)
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for x, y in directions:
                row = i+x
                col = j+y
                if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                    queue.append((row,col,dist+1))
                    grid[row][col] = 2
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1

        return ans


        