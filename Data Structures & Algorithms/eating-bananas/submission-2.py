import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        def time(k):
            ans = 0
            for p in piles:
                ans += math.ceil(p/k)
            return ans

        while left <= right:
            k =(left+right) // 2
            if time(k) <= h:
                right = k-1
            elif time(k) > h:
                left = k+1
        
        return left