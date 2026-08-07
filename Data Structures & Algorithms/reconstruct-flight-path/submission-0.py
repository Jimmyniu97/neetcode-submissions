from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)
        
        for src in adj:
            adj[src].sort()
        
        path = []

        def dfs(node):
            while adj[node]:
                nei = adj[node].pop(0)
                dfs(nei)
            
            path.append(node)
        
        dfs("JFK")
        return path[::-1]