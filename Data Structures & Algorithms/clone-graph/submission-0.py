"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.visited = dict()
        def dfs(node):
            if node in self.visited:
                return self.visited[node]
            
            if not node:
                return
            
            clonedNode = Node(node.val)
            self.visited[node] = clonedNode
            for neighbor in node.neighbors:
                clonedNode.neighbors.append(dfs(neighbor))
            
            return self.visited[node]
        
        return dfs(node)