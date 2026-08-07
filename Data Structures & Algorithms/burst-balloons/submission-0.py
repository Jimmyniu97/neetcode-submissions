class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = dict()
        def dfs(l, r):
            if l > r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            res = 0
            for i in range(l,r+1):
                curr = nums[i] * nums[l-1] * nums[r+1]
                res = max(res, curr+dfs(l, i-1)+dfs(i+1, r))
            dp[(l,r)] = res
            return res
        
        return dfs(1, len(nums)-2)