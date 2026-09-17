class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = dict()

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in cache:
                return cache[amount]
            res = float("INF")
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1+dfs(amount-coin))
            cache[amount] = res
            return res
        
        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins