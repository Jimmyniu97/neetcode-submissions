import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        heap = []
        for i in range(k):
            heapq.heappush(heap, [-nums[i], i])
        res = [-heap[0][0]]
        
        for right in range(k, len(nums)):
            heapq.heappush(heap, [-nums[right], right])
            left += 1
            while heap[0][1] < left:
                heapq.heappop(heap)
            res.append(-heap[0][0])
        return res

