class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = dict()
        def dfs(i):
            if i == len(nums)-1:
                return True
            if i in cache:
                return cache[i]
            if nums[i] == 0:
                return False
            res = False
            for i in range(i+1, min(i+nums[i]+1, len(nums))):
                if dfs(i):
                    res = True
                    break
            cache[i] = res
            return res
        
        return dfs(0)