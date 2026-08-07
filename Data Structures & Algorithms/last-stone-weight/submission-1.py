import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        

        while len(heap) > 1:
            one = -heapq.heappop(heap)
            two = -heapq.heappop(heap)

            if one == two:
                continue
            else:
                heapq.heappush(heap, -(max(one, two)-min(one, two)))
            
        return -heap[0] if len(heap) == 1 else 0