class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        cache = dict()
        for idx, val in enumerate(numbers):
            diff = target - val
            if diff in cache:
                return [cache[diff]+1, idx+1]
            cache[val] = idx
        
        return []