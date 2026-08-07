from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        buckets = [[] for _ in range(len(nums))]
        result = []
        for key, value in counter.items():
            buckets[value-1].append(key)
        
        for i in range(len(buckets)-1, -1, -1):
            length = len(buckets[i])
            if length > 0:
                if length >= k:
                    result.extend(buckets[i][:k])
                    return result
                else:
                    k -= length
                    result.extend(buckets[i])
                
