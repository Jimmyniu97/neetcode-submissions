class Solution:
    class DSU:
        def __init__(self, n):
           self.parent = [i for i in range(n)]
           self.rank = [1] * n
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        def union(self, a, b):
            rootA = self.find(a)
            rootB = self.find(b)
            if rootA == rootB:
                return False 
            if self.rank[rootA] > self.rank[rootB]:
                self.parent[rootB] = rootA
            elif self.rank[rootA] < self.rank[rootB]:
                self.parent[rootA] = rootB
            else:
                self.parent[rootB] = rootA
                self.rank[rootA] += 1
            return True

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = self.DSU(n)
        res = [-1, -1]
        for u, v in edges:
            if not dsu.union(u-1, v-1):
                res = [u, v]
        
        return res
