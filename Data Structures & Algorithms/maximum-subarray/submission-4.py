class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, curr = nums[0], 0
        for num in nums:
            if curr < 0:
                curr = 0
            curr += num
            ans = max(ans, curr)
        
        return ans