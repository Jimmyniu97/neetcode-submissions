class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        accessPacific = []
        accessAtlantic = []
        ROWS = len(heights)
        COLS = len(heights[0])

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    accessPacific.append((r,c))
                if r == ROWS-1 or c == COLS-1:
                    accessAtlantic.append((r,c))
        
        def bfs(position):
            queue = collections.deque(position)
            visited = set(p for p in position)
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            while queue:
                qLen = len(queue)
                for _ in range(qLen):
                    r, c = queue.popleft()
                    for dr, dc in directions:
                        i, j = r+dr, c+dc
                        if (0 <= i < ROWS and 0 <= j < COLS and (i,j) not in visited and heights[i][j] >= heights[r][c]):
                            queue.append((i,j))
                            visited.add((i,j))
            
            return visited
        

        aFlow = bfs(accessAtlantic)
        pFlow = bfs(accessPacific)
        return list(aFlow.intersection(pFlow))
