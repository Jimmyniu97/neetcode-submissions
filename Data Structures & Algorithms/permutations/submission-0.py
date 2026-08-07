class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], nums, [False]*len(nums))
        return self.res

    def backtrack(self, perm, nums, choose):
        if len(perm) == len(nums):
            self.res.append(perm.copy())
            return
        
        for i in range(len(nums)):
            if not choose[i]:
                perm.append(nums[i])
                choose[i] = True
                self.backtrack(perm, nums, choose)
                choose[i] = False
                perm.pop()