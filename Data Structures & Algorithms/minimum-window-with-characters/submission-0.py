from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cache_t = Counter(t)
        formed = 0
        window = defaultdict(int)
        left = 0
        resLen = math.inf
        res = [-1, -1]
        for right in range(len(s)):
            window[s[right]] += 1
            if s[right] in cache_t and window[s[right]] == cache_t[s[right]]:
                formed += 1
            
            while formed == len(cache_t):
                if (right-left+1) < resLen:
                    resLen = right-left+1
                    res = [left, right]
                
                window[s[left]] -= 1
                if s[left] in cache_t and window[s[left]] < cache_t[s[left]]:
                    formed -= 1
                left += 1
        
        left, right = res
        return s[left:right+1] if resLen != math.inf else ""
