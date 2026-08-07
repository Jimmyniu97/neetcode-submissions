class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = dict()

        def dfs(i, canBuy):
            if i >= len(prices):
                return 0
            
            if (i, canBuy) in dp:
                return dp[(i,canBuy)]
            
            if canBuy:
                dp[(i,canBuy)] = max(-prices[i]+dfs(i+1, False), dfs(i+1, True))
            else:
                dp[(i,canBuy)] = max(prices[i]+dfs(i+2, True), dfs(i+1, False))
            
            return dp[(i,canBuy)]
        
        return dfs(0, True)