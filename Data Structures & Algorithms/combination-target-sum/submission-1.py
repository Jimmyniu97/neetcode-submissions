class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(idx, curr):
            if sum(curr) == target:
                res.append(curr.copy())
                return
            if idx >= len(nums) or sum(curr) > target:
                return
            
            dfs(idx, curr+[nums[idx]])
            dfs(idx+1, curr)
            
        
        dfs(0, [])
        return res