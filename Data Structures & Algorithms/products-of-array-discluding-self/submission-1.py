class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        result = [1] * len(nums)
        left[0] = 1
        right[-1] = 1

        for i in range(1, len(nums)):
            num = nums[i-1]
            left[i] = num * left[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            num = nums[i+1]
            right[i] = num * right[i+1]
        
        for i in range(len(nums)):
            result[i] = left[i] * right[i]
        
        return result
