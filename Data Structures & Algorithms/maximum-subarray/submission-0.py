class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        currSum = nums[0]
        currMax = nums[0]

        for i in range(1, n):
            currSum = max(nums[i], currSum+nums[i])
            currMax = max(currMax, currSum)
        
        return currMax
            
            