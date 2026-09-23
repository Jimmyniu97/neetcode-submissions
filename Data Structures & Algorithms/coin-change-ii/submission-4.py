class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = dict()

        def dfs(i, a):
            if i >= len(coins):
                return 0
            if a == amount:
                return 1
            if (i, a) in cache:
                return cache[(i, a)]
            
            res = dfs(i+1, a)
            if coins[i] + a <= amount:
                res += dfs(i, coins[i]+a)
            
            
            cache[(i, a)] = res
            return res
        
        return dfs(0, 0)