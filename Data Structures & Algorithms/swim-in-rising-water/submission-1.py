import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        board = [float("INF") * n for _ in range(n)]
        heap = [(grid[0][0], 0, 0)]
        visited = {(0,0)}
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        while heap:
            height, r, c = heapq.heappop(heap)
            if r == n-1 and c == n-1:
                return height
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if (0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited):
                    visited.add((nr, nc))
                    newHeight = max(height, grid[nr][nc])
                    heapq.heappush(heap, (newHeight, nr, nc))
            