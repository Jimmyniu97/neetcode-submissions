class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = dict()
        for index, value in enumerate(nums):
            difference = target - value
            if difference in cache:
                return [cache[difference], index]
            cache[value] = index