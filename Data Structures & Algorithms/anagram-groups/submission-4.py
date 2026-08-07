class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = dict()
        for token in strs:
            split_token = tuple(sorted(list(token)))
            if split_token not in cache:
                cache[split_token] = [token]
            else:
                cache[split_token].append(token)
        
        return list(cache.values())