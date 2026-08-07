class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        def dfs(i, j):
            if i >= n:
                return 0
            if dp[i][j] != 0:
                return dp[i][j]
            ans = 0
            if j == -1 or nums[i] > nums[j]:
                ans = max(ans, 1+dfs(i+1, i))
            ans = max(ans, dfs(i+1, j))
            dp[i][j] = ans
            return ans

        return dfs(0, -1)