import heapq
from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []

        for p in points:
            dist = math.sqrt(p[0]**2+p[1]**2)
            heapq.heappush(heap, (-dist, p))
            if len(heap) > k:
                heapq.heappop(heap)
        
        while heap:
            top = heapq.heappop(heap)[1]
            res.append(top)

        
        return res