class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        current = []
        def dfs(i):
            if i >= len(nums):
                res.append(current.copy())
                return
            
            current.append(nums[i])
            dfs(i+1)
            current.pop()

            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1)
        
        dfs(0)
        return res