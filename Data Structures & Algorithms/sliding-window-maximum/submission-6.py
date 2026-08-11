from collections import deque
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = 0
        heap = []
        for right in range(len(nums)):
            window += 1
            heapq.heappush(heap, (-nums[right], right))
            if window == k:
                while heap[0][1] <= right-k:
                    heapq.heappop(heap)
                result.append(-heap[0][0])
                window -= 1
        
        return result

