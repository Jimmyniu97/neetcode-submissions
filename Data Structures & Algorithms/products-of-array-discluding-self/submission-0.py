class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        left[0] = nums[0]
        for i in range(1, len(nums)):
            left[i] = nums[i]*left[i-1]
        
        right = [1]*len(nums)
        right[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            right[i] = (nums[i]*right[i+1])
        
        result = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                result[i] = right[i+1]
            elif i == len(nums)-1:
                result[i] = left[i-1]
            else:
                result[i] = left[i-1] * right[i+1]
        return result
