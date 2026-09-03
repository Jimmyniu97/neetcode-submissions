class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(curr, contains):
            if sum(contains) == len(nums):
                res.append(curr.copy())
                return
            for i in range(len(contains)):
                if not contains[i]:
                    contains[i] = True
                    dfs(curr+[nums[i]], contains)
                    contains[i] = False

        contains = [False] * len(nums)
        dfs([], contains)
        return res                