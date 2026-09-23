class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = dict()
        def dfs(i, canBuy):
            if i >= len(prices):
                return 0
            if (i, canBuy) in cache:
                return cache[(i, canBuy)]
            
            res = dfs(i+1, canBuy)
            if canBuy:
                res = max(res, -prices[i]+dfs(i+1, False))
            else:
                res = max(res, prices[i]+dfs(i+2, True))

            cache[(i, canBuy)] = res
            return res
        
        return dfs(0, True)