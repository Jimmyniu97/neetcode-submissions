class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = dict()
        def dfs(i, j):
            k = i+j
            if k >= len(s3):
                return True
            
            if (i,j) in dp:
                return dp[(i,j)]
            res = False
            
            if i < len(s1) and s3[k] == s1[i]:
                res = res or dfs(i+1, j)
            if j < len(s2) and s3[k] == s2[j]:
                res = res or dfs(i, j+1)
            dp[(i,j)] = res
            return dp[(i,j)]
        
        return dfs(0,0)