class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = dict({i:[] for i in range(n)})
        visited = set()
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def bfs(node):
            queue = collections.deque([node])
            visited.add(node)
            while queue:
                cur = queue.popleft()
                for nei in adj[cur]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
        
        res = 0
        for node in range(n):
            if node not in visited:
                bfs(node)
                res += 1
        
        return res
