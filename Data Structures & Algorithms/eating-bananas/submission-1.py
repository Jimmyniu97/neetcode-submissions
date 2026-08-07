import math
class Solution:
    def countHour(self, piles, k):
        ans = 0
        for pile in piles:
            ans += math.ceil(pile/k)
        return ans

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = right
        while left <= right:
            mid = (left+right) // 2
            if self.countHour(piles, mid) > h:
                left = mid + 1
            else:
                right = mid - 1
                ans = mid
        return ans
