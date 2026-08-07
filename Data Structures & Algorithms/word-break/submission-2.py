class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        cache = [None] * n
        def dfs(i):
            if i == n:
                return True
            if cache[i] is not None:
                return cache[i]

            for word in wordDict:
                if s[i:].startswith(word):
                    length = len(word)
                    if dfs(i+length):
                        cache[i] = True
                        return True
            cache[i] = False
            return False
        
        return dfs(0)
