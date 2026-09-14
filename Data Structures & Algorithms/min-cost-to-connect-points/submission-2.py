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

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dsu = self.DSU(n)
        edges = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                edges.append((dist, i, j))
        
        edges.sort()
        res = 0
        for dist, u, v in edges:
            if dsu.union(u, v):
                res += dist
        return res
