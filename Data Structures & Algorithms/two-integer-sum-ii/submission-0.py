class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        cache = dict()
        for index, value in enumerate(numbers):
            diff = target - value
            if diff in cache:
                return [cache[diff]+1, index+1]
            cache[value] = index