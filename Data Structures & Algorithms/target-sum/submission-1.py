class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = dict()
        def dfs(i, total):
            if i >= len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            if (i, total) in cache:
                return cache[(i, total)]
            cache[(i, total)] = dfs(i+1, total-nums[i]) + dfs(i+1, total+nums[i])
            return cache[(i, total)]
        
        return dfs(0, 0)