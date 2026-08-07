class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount+1)
        dp[0] = 0
        for a in range(1, amount+1):
            for i in range(len(coins)):
                if a - coins[i] >= 0:
                    dp[a] = min(dp[a], 1+dp[a-coins[i]])
        
        return dp[amount] if dp[amount] != math.inf else -1