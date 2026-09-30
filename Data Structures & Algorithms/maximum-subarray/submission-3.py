class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        current = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > current+nums[i]:
                current = nums[i]
            else:
                current += nums[i]
            ans = max(ans, current)
        
        return ans