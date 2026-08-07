from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        counterS = Counter(s)
        counterT = Counter(t)

        for val in counterS:
            if val not in counterT or counterS[val] != counterT[val]:
                return False
        
        return True