from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31-1

        queue = deque()
        visited = set()
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i,j,0))
        
        while queue:
            i, j, dist = queue.popleft()
            visited.add((i,j))
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            if grid[i][j] == INF:
                grid[i][j] = dist

            for x,y in directions:
                row = i+x
                col = j+y
                if 0 <= row < rows and 0 <= col < cols and (row, col) not in visited and grid[row][col] == INF:
                    queue.append((row,col, dist+1))
        


        
            