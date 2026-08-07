from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_s1 = Counter(s1)
        window_cache = defaultdict(int)
        left = 0
        formed = 0
        for right in range(len(s2)):
            window_cache[s2[right]] += 1
            while right-left+1 > len(s1):
                window_cache[s2[left]] -= 1
                if window_cache[s2[left]] == 0:
                    del window_cache[s2[left]]
                left += 1

            if window_cache == counter_s1:
                return True
        
        return False
            

            
