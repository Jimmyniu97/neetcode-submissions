class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0] * (n+1)
        dp[n] = 0
        dp[n-1] = 0

        for i in range(n-2, -1, -1):
            dp[i] = max(nums[i]+dp[i+2], dp[i+1])
        
        dp2 = [0] * (n+2)
        dp2[n] = 0
        dp2[n+1] = 0

        for i in range(n-1, 0, -1):
            dp2[i] = max(nums[i]+dp2[i+2], dp2[i+1])
        
        return max(dp[0], dp2[1])
        


