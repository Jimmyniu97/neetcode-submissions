from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter_s = Counter(s)
        counter_t = Counter(t)

        for value in counter_s:
            if value not in counter_t or counter_s[value] != counter_t[value]:
                return False
        
        return True