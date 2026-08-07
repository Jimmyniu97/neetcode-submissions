class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, curr, currSum):
            if currSum == target:
                res.append(curr.copy())
                return
            if currSum > target or i == len(candidates):
                return
            
            curr.append(candidates[i])
            dfs(i+1, curr, currSum+candidates[i])
            curr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, curr, currSum)
        
        dfs(0, [], 0)
        return res