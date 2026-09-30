class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid = [False] * 3

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            if t[0] == target[0]:
                valid[0] = True
            if t[1] == target[1]:
                valid[1] = True
            if t[2] == target[2]:
                valid[2] = True
        
        return sum(valid) == 3