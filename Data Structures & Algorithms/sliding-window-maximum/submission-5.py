from collections import deque
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = deque()
        heap = []
        for right in range(len(nums)):
            window.append(nums[right])
            heapq.heappush(heap, (-nums[right], right))
            if len(window) == k:
                while heap[0][1] <= right-k:
                    heapq.heappop(heap)
                result.append(-heap[0][0])
                window.popleft()
        
        return result

