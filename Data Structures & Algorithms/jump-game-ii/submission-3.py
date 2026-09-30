class Solution:
    def jump(self, nums: List[int]) -> int:
        cache = dict()
        def dfs(i):
            if i >= len(nums)-1:
                return 0
            if i in cache:
                return cache[i]
            if nums[i] == 0:
                return 10000
            res = 10000
            for j in range(i+1, min(i+nums[i]+1, len(nums))):
                res = min(res, 1+ dfs(j))
            cache[i] = res
            return res
        
        return dfs(0)