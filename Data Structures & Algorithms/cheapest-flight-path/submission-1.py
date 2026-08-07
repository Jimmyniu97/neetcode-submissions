class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [math.inf] * n
        dist[src] = 0

        for _ in range(k+1):
            temp = dist.copy()
            for u, v, price in flights:
                if dist[u] != math.inf and dist[u] + price < temp[v]:
                    temp[v] = dist[u] + price
            dist = temp
        
        return -1 if dist[dst] == math.inf else dist[dst]