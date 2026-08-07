class Solution:
    def bfs(self, grid, i, j):
        queue = [[i,j]]
        m = len(grid)
        n = len(grid[0])
        grid[i][j] = "0"
        while queue:
            current = queue.pop()
            r, c = current[0], current[1]
            for x, y in [(-1,0),(1,0),(0,-1),(0,1)]:
                row = r + x
                col = c + y
                if 0 <= row < m and 0 <= col < n and grid[row][col] == "1":
                    queue.append([row, col])
                    grid[row][col] = "0"

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.bfs(grid, i, j)
                    count += 1
        
        return count