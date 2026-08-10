from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        ans = 0
        maxF = 0
        cache = defaultdict(int)
        for right in range(len(s)):
            cache[s[right]] += 1
            maxF =  max(cache.values())
            while (right-left+1) - maxF > k:
                cache[s[left]] -= 1
                left += 1
            ans = max(ans, right-left+1)
        
        return ans