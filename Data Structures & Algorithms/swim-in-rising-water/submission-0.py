class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        heap = [(grid[0][0], 0, 0)]
        direction = [[0,1],[0,-1],[1,0],[-1,0]]

        while heap:
            elevation, r, c = heapq.heappop(heap)
            if (r, c) in visited:
                continue
            
            visited.add((r, c))

            if r == n-1 and c == n-1:
                return elevation
            
            for x, y in direction:
                row = r+x
                col = c+y
                if 0 <= row < n and 0 <= col < n and (row, col) not in visited:
                    newElevation = max(elevation, grid[row][col])
                    heapq.heappush(heap, (newElevation, row, col))