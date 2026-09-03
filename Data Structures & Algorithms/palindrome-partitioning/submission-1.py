class Solution:
    def isPalin(self, word):
        return word == word[::-1]

    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(curr, j ,i):
            if i >= len(s):
                if j >= len(s):
                    res.append(curr)
                return
            
            if self.isPalin(s[j:i+1]):
                dfs(curr+[s[j:i+1]], i+1, i+1)
            dfs(curr, j, i+1)
            
        
        dfs([], 0, 0)
        return res