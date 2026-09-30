class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cache = dict()
        res = []
        for idx, value in enumerate(s):
            cache[value] = idx
        size = end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, cache[c])

            if i == end:
                res.append(size)
                size = 0
        
        return res