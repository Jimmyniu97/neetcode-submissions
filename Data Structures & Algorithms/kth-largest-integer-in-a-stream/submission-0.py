import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            heapq.heappush(self.heap, -num)


    def add(self, val: int) -> int:
        temp = []
        heapq.heappush(self.heap, -val)
        for _ in range(self.k-1):
            temp.append(heapq.heappop(self.heap))
        ans = -self.heap[0]
        self.heap.extend(temp)
        heapq.heapify(self.heap)
        return ans
