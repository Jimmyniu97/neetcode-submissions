class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cache = dict()
        left = 0
        ans = 0
        max_freq = 0
        for right in range(len(s)):
            cache[s[right]] = cache.get(s[right], 0) + 1
            max_freq = max(max_freq, cache[s[right]])
            #max number of replacement = window length - frequency of most frequent element
            while right-left+1-max_freq > k:
                cache[s[left]] -= 1
                left += 1
            ans = max(ans, right-left+1)
            

        return ans   