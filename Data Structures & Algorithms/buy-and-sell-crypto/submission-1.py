class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        ans = 0
        for right in range(1, len(prices)):
            if prices[right] > prices[left]:
                ans = max(ans, prices[right]-prices[left])
            elif prices[right] < prices[left]:
                left = right
        
        return ans