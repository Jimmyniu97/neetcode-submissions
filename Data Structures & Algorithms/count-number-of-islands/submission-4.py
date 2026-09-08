class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):
            grid[r][c] = '0'
            stack = [(r, c)]
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while stack:
                row, col = stack.pop()
                for x, y in directions:
                    i, j = row+x, col+y
                    if (0 <= i < ROWS and 0 <= j < COLS and grid[i][j] == '1'):
                        grid[i][j] = '0'
                        stack.append((i, j))
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(r, c)
                    res += 1
        
        return res
