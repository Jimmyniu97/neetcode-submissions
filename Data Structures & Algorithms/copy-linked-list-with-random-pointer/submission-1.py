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
        curr = head
        dummy = node = Node(-1)
        while curr:
            node.next = Node(curr.val)
            cache[curr] = node.next
            curr = curr.next
            node = node.next
        
        curr = head
        while curr:
            copyNode = cache[curr]
            copyNode.random = cache[curr.random] if curr.random else None
            curr = curr.next
        
        return dummy.next
        
        
