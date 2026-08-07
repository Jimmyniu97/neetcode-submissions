# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sameTree(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False
        elif root1.val != root2.val:
            return False
        
        return self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return False
            if self.sameTree(root, subRoot):
                return True
            return dfs(root.left) or dfs(root.right)
        
        if not subRoot:
            return True
        return dfs(root)