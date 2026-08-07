from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]
        result = []

        for key, value in counter.items():
            bucket[value].append(key)
        
        for i in range(len(bucket)-1, -1, -1):
            if len(result) >= k:
                break
            for num in bucket[i]:
                if len(result) < k:
                    result.append(num)
        
        return result
                