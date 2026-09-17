class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = [None] * len(s)
        def dfs(i):
            if i >= len(s):
                return True
            if cache[i] != None:
                return cache[i]
            res = False
            for w in wordDict:
                wLen = len(w)
                if s[i:i+wLen] == w and dfs(i+wLen):
                    res = True
                    break
            cache[i] = res
            return res
        
        return dfs(0)