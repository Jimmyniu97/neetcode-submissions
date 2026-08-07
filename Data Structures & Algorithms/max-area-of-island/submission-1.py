class Solution:
    def bfs(self, i, j, grid):
        grid[i][j] = 0
        stack = [[i,j]]
        count = 0
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        while stack:
            curr = stack.pop()
            count += 1
            for x,y in directions:
                row = curr[0]+x
                col = curr[1]+y
                if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1:
                    stack.append([row, col])
                    grid[row][col] = 0
        
        return count

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans = max(ans, self.bfs(i, j, grid))
        
        return ans