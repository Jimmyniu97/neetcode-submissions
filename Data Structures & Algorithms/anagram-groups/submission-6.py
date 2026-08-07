from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = defaultdict(list)
        result = []
        for s in strs:
            counter = [0] * 26
            for c in s:
                val = ord(c) - ord('a')
                counter[val] += 1
            cache[tuple(counter)].append(s)
        
        for sortedS in cache:
            result.append([s for s in cache[sortedS]])
        
        return result
