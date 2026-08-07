class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        l, r = 0, nums[0]
        count = 1
        while r < len(nums)-1:
            currMax = 0
            for i in range(l, r+1):
                currMax = max(currMax, i+nums[i])
            l = r+1
            r = currMax
            count += 1
        
        return count
