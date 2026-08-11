from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        cache = defaultdict(int)
        counterT = Counter(t)
        left = 0
        minLen = math.inf
        ans = [-1, -1]
        have, need = 0, len(counterT)

        for right in range(len(s)):
            cache[s[right]] += 1
            if s[right] in counterT and cache[s[right]] == counterT[s[right]]:
                have += 1
            
            while have == need:
                if (right-left+1) < minLen:
                    minLen = right-left+1
                    ans = [left, right]

                cache[s[left]] -= 1
                if s[left] in counterT and cache[s[left]] < counterT[s[left]]:
                    have -= 1
                left += 1

        l, r = ans
        return "" if minLen == math.inf else s[l:r+1]