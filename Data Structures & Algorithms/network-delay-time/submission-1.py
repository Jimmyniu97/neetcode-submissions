import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))
        
        heap = [(0, k)]
        dist = dict()

        while heap:
            d, node = heapq.heappop(heap)
            if node in dist:
                continue
            dist[node] = d
            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(heap, (d+d2, nei))
        
        return max(dist.values()) if len(dist) == n else -1