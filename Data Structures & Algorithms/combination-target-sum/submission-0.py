class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        def dfs(i, currentSum):
            if currentSum == target:
                result.append(path.copy())
                return
            
            for index in range(i, len(nums)):
                if currentSum + nums[index] <= target:
                    path.append(nums[index])
                    dfs(index, currentSum+nums[index])
                    path.pop()
        
        dfs(0, 0)
        return result