# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node, maximum):
            if not node:
                return
            
            if node.val >= maximum:
                maximum = max(node.val, maximum)
                self.ans += 1
            dfs(node.left, maximum)
            dfs(node.right, maximum)
        
        dfs(root, root.val)
        return self.ans