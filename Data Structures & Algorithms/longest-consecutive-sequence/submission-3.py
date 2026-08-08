class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cache = set(nums)
        ans = 0

        for i in range(len(nums)):
            count = 1
            if nums[i]-1 not in cache:
                start = nums[i]
                while start+1 in cache:
                    count += 1
                    start += 1
                ans = max(ans, count)
        
        return ans