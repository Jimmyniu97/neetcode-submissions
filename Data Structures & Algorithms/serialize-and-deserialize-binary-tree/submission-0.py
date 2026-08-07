# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.ans = ""
        def dfs(root):
            if not root:
                self.ans += ",N" if self.ans else "N"
                return
            self.ans += "," + str(root.val) if self.ans else str(root.val) 
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.ans

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodeList = data.split(",")
        if len(nodeList) == 0:
            return None
        self.idx = 0
        def dfs():
            if nodeList[self.idx] == "N":
                self.idx += 1
                return None
            node = TreeNode(nodeList[self.idx])
            self.idx += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()
        
