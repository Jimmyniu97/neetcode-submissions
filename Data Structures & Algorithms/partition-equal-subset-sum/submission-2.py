class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        cache = dict()
        def dfs(i, curSum):
            if i >= len(nums):
                return False
            if curSum == total // 2:
                return True
            if (i, curSum) in cache:
                return cache[(i, curSum)]
            res = dfs(i+1, curSum)
            if curSum < total // 2:
                res = res or dfs(i+1, curSum + nums[i])
            cache[(i, curSum)] = res
            return res
        
        return dfs(0, 0)