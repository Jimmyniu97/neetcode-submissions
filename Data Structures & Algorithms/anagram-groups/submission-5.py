from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = defaultdict(list)
        result = []
        for s in strs:
            listS = tuple(sorted(list(s)))
            cache[listS].append(s)
        
        for sortedS in cache:
            result.append([s for s in cache[sortedS]])
        
        return result
