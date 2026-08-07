class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, a):
        if self.parent[a] == a:
            return a
        return self.find(self.parent[a])
    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA == rootB:
            return False

        self.parent[rootA] = rootB
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = n
        dsu = DSU(n)

        for a, b in edges:
            if dsu.union(a, b):
                res -= 1
        
        return res

        
                