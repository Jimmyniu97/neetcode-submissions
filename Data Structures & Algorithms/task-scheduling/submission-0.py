from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency = Counter(tasks)
        time = 0
        heap = [-cnt for cnt in frequency.values()]
        heapq.heapify(heap)
        queue = deque()

        while heap or queue:
            time += 1
            if not heap:
                time = queue[0][1]
            else:
                current = 1 + heapq.heappop(heap)
                if current < 0:
                    queue.append([current, time+n])
            
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
            
        
        return time