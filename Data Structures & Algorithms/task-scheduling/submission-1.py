import heapq
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        queue = deque()
        time = 0

        heap = [-val for val in counter.values()]
        heapq.heapify(heap)

        while heap or queue:
            time += 1
            if not heap:
                time = queue[0][1]
            else:
                freq = heapq.heappop(heap)
                freq += 1
                if freq != 0:
                    queue.append((freq, time+n))
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
        
        return time
