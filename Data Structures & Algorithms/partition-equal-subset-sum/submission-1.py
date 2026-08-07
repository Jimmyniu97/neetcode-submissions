class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        cache = {}
        if total % 2 != 0:
            return False

        def dfs(i, currSum):
            if i >= len(nums) or currSum > total//2:
                return False
            
            if currSum == total // 2:
                return True
            
            if (i, currSum) in cache:
                return cache[(i, currSum)]
            
            take = dfs(i+1, currSum+nums[i])
            skip = dfs(i+1, currSum)

            cache[(i, currSum)] = take or skip
            return cache[(i, currSum)]
        
        return dfs(0, 0)
            

            
