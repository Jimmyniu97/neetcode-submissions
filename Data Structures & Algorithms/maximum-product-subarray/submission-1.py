class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        ansMax = -math.inf
        cache = [[] for _ in range(len(nums))]
        cache[0].extend([nums[0], nums[0]])

        for i in range(1, len(nums)):
            currMax = max(nums[i], nums[i] * cache[i-1][0], nums[i] * cache[i-1][1])
            currMin = min(nums[i], nums[i] * cache[i-1][0], nums[i] * cache[i-1][1])
            ansMax = max(ansMax, currMax)
            cache[i].extend([currMax, currMin])

        return ansMax   