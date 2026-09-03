class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(idx, subset):
            if idx >= len(nums):
                res.append(subset.copy())
                return
            dfs(idx+1, subset+[nums[idx]])
            i = 1
            while idx + i < len(nums) and nums[idx] == nums[idx+i]:
                i += 1
            dfs(idx+i, subset)
        
        dfs(0, [])
        return res