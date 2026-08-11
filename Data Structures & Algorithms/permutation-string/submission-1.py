from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counterS1 = Counter(s1)
        counterS2 = defaultdict(int)
        left = 0
        for right in range(len(s2)):
            counterS2[s2[right]] += 1
            if right-left+1 > len(s1):
                counterS2[s2[left]] -= 1
                if counterS2[s2[left]] == 0:
                    del counterS2[s2[left]]
                left += 1
            
            if counterS2 == counterS1:
                return True
        
        return False
        