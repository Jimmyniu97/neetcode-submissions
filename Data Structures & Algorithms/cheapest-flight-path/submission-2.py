import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float("INF")
        prices = [INF] * n
        prices[src] = 0

        for _ in range(k+1):
            temp = prices.copy()
            for u, v, p in flights:
                if prices[u] == INF:
                    continue
                if prices[u] + p < temp[v]:
                    temp[v] = prices[u] + p
            prices = temp
        
        return -1 if prices[dst] == INF else prices[dst]
        
        
