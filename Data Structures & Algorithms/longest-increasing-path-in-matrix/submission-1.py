class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = dict()
        ROWS = len(matrix)
        COLS = len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j, prev):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or matrix[i][j] <= prev:
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            res = 1
            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                res = max(res, 1+dfs(nr, nc, matrix[i][j]))
            cache[(i, j)] = res
            return res


        
        ans = 0
        for i in range(ROWS):
            for j in range(COLS):
                ans = max(ans, dfs(i ,j, -1))
        
        return ans