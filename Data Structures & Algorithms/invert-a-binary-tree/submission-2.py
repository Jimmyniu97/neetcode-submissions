# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            if curr:
                left = curr.left
                right = curr.right
                curr.left, curr.right = right, left
                queue.append(right)
                queue.append(left)
        
        return root
