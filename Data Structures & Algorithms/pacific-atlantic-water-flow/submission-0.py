class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        def dfs(i, j, visited):
            if (i,j) in visited:
                return

            visited.add((i,j))
            
            for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                row = i + x
                col = j + y
                if (0 <= row < len(heights) and 0 <= col < len(heights[0])) and heights[row][col] >= heights[i][j]:
                    dfs(row, col, visited)
            
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    dfs(i, j, pacific)
                if i == len(heights)-1 or j == len(heights[0])-1:
                    dfs(i, j, atlantic)
        
        result = []
        for cell in pacific.intersection(atlantic):
            result.append(list(cell))
        return result