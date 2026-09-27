class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        cache = dict()
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in cache:
                return cache[(l, r)]
            
            best = 0
            for i in range(l, r+1):
                res =  nums[l-1] * nums[i] * nums[r+1] + dfs(l, i-1) + dfs(i+1, r)
                best = max(best, res)
            cache[(l, r)] = best
            return best
        
        return dfs(1, len(nums)-2)
