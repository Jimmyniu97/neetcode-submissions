class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(idx, curr):
            if sum(curr) == target:
                res.append(curr.copy())
                return
            if idx >= len(candidates) or sum(curr) > target:
                return
            
            dfs(idx+1, curr + [candidates[idx]])
            i = 1
            while idx+i < len(candidates) and candidates[idx] == candidates[idx+i]:
                i += 1
            dfs(idx+i, curr)
        
        dfs(0, [])
        return res