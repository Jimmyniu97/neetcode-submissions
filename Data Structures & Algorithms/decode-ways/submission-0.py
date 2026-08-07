class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        cache = {}
        def dfs(i):
            if i >= n:
                return 1
            if s[i] == '0':
                return 0
            if i in cache:
                return cache[i]
            
            ans = dfs(i+1)
            if i < n - 1 and 10 <= int(s[i:i+2]) <= 26:
                ans += dfs(i+2)
            
            cache[i] = ans
            return ans
        
        return dfs(0)
            
            