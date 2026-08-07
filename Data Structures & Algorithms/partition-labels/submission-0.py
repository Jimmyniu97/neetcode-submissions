class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cache = dict()
        for index, value in enumerate(s):
            cache[value] = index
        size = end = 0
        res = []

        for index, value in enumerate(s):
            size += 1
            end = max(end, cache[value])

            if index == end:
                res.append(size)
                size = 0
        return res
        