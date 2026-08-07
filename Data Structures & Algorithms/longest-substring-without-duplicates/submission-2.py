class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = dict()
        left = 0
        ans = 0
        for right in range(len(s)):
            if s[right] not in cache:
                cache[s[right]] = right
            else:
                left = max(left, cache[s[right]] + 1)
                cache[s[right]] = right
            ans = max(ans, right-left+1)
        return ans