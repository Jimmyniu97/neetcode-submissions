from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = Counter(s)
        counter_t = Counter(t)

        if len(counter_s) != len(counter_t):
            return False

        for c in counter_s:
            if c not in counter_t or counter_s[c] != counter_t[c]:
                return False
        
        return True