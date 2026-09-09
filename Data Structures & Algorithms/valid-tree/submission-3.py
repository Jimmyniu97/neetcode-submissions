class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = dict({i:[] for i in range(n)})

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        
        def dfs(node, par):
            if node in visited:
                return False
            visited.add(node)
            for nei in graph[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True
            
        return dfs(0, -1) and len(visited) == n
        
        
        
        