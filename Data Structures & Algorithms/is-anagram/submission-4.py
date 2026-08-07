class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sortS = sorted(list(s))
        sortT = sorted(list(t))

        for i in range(len(sortS)):
            if sortS[i] != sortT[i]:
                return False
        
        return True
