class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str = ["".join(sorted(string)) for string in strs]
        cache = dict()
        for index, value in enumerate(sorted_str):
            if value not in cache:
                cache[value] = [index]
            else:
                cache[value].append(index)
        
        result = []
        for string in cache:
            temp_list = []
            for index in cache[string]:
                temp_list.append(strs[index])
            result.append(temp_list)
        return result