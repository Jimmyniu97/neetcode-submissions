# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        cache = dict()
        for i, v in enumerate(inorder):
            cache[v] = i
        self.idx = 0

        def dfs(l, r):
            if self.idx >= len(preorder):
                return
            if l > r:
                return
            val = preorder[self.idx]
            j = cache[val]
            self.idx += 1

            node = TreeNode(val)
            node.left = dfs(l, j-1)
            node.right = dfs(j+1, r)

            return node
        
        return dfs(0, len(inorder)-1)