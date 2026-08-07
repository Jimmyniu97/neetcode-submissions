class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edge = dict({i:[] for i in range(n+1)})
        for t in times:
            edge[t[0]].append([t[1], t[2]])
        
        heap = []
        heapq.heappush(heap, (0, k))
        dist = [math.inf] * (n+1)
        dist[k] = 0

        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, w in edge[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (dist[v], v))
        
        ans = 0
        for d in dist[1:]:
            if d == math.inf:
                return -1
            ans = max(ans, d)
        return ans
        
        
