class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        cache = {n: 1}

        def dfs(i):
            if i in cache:
                return cache[i]
            if s[i] == '0':
                return 0
            
            cache[i] = dfs(i+1)
            if 10 <= int(s[i:i+2]) <= 26:
                cache[i] += dfs(i+2)
            
            return cache[i]

        return dfs(0)