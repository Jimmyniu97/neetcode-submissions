class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = dict()
        def dfs(i, j):
            if i >= rows or j >= cols:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            res = 1
            
            for x,y in [[1,0],[-1,0],[0,1],[0,-1]]:
                row = x+i
                col = y+j
                if 0 <= row < rows and 0 <= col < cols and matrix[row][col] > matrix[i][j]:
                    res = max(res, 1+dfs(row, col))
            
            dp[(i,j)] = res
            return dp[(i,j)]
        
        ans = 0
        for i in range(rows):
            for j in range(cols):
                ans = max(ans, dfs(i,j))
        
        return ans