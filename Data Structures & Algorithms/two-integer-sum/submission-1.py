class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = dict()
        for index, value in enumerate(nums):
            diff = target - value
            if diff in cache:
                return [cache[diff], index]
            cache[value] = index
        
        return []