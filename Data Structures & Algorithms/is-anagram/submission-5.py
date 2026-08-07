from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterS = Counter(s)
        counterT = Counter(t)

        if counterS.keys() != counterT.keys():
            return False

        for val in counterS:
            if counterS[val] != counterT[val]:
                return False
        
        return True