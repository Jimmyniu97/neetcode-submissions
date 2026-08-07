from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = defaultdict(list)
        for string in strs:
            counter = [0] * 26
            for character in string:
                value = ord(character) - ord('a')
                counter[value] += 1
            counter = tuple(counter)
            cache[counter].append(string)
                
        
        result = [cache[counter] for counter in cache]
        return result