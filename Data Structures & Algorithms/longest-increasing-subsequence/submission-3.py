class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [[-1] * (n+1) for _ in range(n)]

        def dfs(i, j):
            if i >= len(nums):
                return 0
            if cache[i][j] != -1:
                return cache[i][j]
            res = dfs(i+1, j)
            if j == -1 or nums[i] > nums[j]:
                res = max(res, 1 + dfs(i+1, i))
            cache[i][j] = res
            return res
        
        return dfs(0, -1)
            