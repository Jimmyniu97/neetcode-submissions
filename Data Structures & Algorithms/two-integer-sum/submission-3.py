class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = dict()
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in cache:
                return [cache[diff], idx]
            cache[val] = idx
        
        return []