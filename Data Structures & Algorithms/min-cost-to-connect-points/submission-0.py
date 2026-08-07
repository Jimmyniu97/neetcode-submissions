class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [1] * (n+1)
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self, a, b):
        parentA = self.find(a)
        parentB = self.find(b)
        if parentA == parentB:
            return False
        if self.rank[parentA] < self.rank[parentB]:
            self.parent[parentA] = parentB
        elif self.rank[parentA] > self.rank[parentB]:
            self.parent[parentB] = parentA
        else:
            self.parent[parentB] = parentA
            self.rank[parentA] += 1
        return True      
        
 
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                if i != j:
                    dist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                    edges.append((dist, i, j))
        
        edges.sort(key=lambda x:x[0])

        dsu = DSU(len(points))
        totalCost = 0
        edgeUsed = 0

        for cost, u, v in edges:
            if dsu.union(u,v):
                totalCost += cost
                edgeUsed += 1

                if edgeUsed == len(points)-1:
                    break
        
        return totalCost

        