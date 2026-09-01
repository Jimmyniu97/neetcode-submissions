import heapq
class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
    
    def __balance(self):
        if len(self.maxHeap) - len(self.minHeap) > 1:
            top = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -top)
        elif len(self.minHeap) - len(self.maxHeap) > 1:
            top = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -top)

    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        
        self.__balance()

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        elif len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        else:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        