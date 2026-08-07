"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cache = dict()
        def dfs(node):
            if not node:
                return
            
            if node in cache:
                return cache[node]
            
            copyNode = Node(node.val)
            cache[node] = copyNode
            copyNode.next = dfs(node.next)
            copyNode.random = dfs(node.random)
            return copyNode
        
        return dfs(head)