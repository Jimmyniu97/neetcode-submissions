class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return math.inf
            if amount in cache:
                return cache[amount]
            res = math.inf
            for i in range(len(coins)):
                res = min(res, 1 + dfs(amount-coins[i]))
            cache[amount] = res
            return res
        
        ans = dfs(amount)
        return ans if ans != math.inf else -1  