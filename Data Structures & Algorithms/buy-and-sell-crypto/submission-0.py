class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        ans = 0
        for right in range(len(prices)):
            if prices[right] < prices[left]:
                left = right
            if prices[right] - prices[left] > 0:
                ans = max(ans, prices[right] - prices[left])
        return ans