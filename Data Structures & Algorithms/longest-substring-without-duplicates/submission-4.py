class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        cache = set()
        ans = 0
        for right in range(len(s)):
            while s[right] in cache:
                cache.discard(s[left])
                left += 1
            cache.add(s[right])
            ans = max(ans, right-left+1)
        
        return ans