class Solution:
    def myPow(self, x: float, n: int) -> float:
        def dfs(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            if n % 2 == 1:
                return x * dfs(x, (n-1)//2) * dfs(x, (n-1)//2)
            return dfs(x, n//2) * dfs(x, n//2)
        res = dfs(x, abs(n))
        return res if n > 0 else 1/res

