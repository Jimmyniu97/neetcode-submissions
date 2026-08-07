class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in dp:
                return dp[i]
            
            robCurrent = nums[i] + dfs(i+2)
            skipCurrent = dfs(i+1)
            dp[i] = max(robCurrent, skipCurrent)
            return dp[i]
        
        return dfs(0)